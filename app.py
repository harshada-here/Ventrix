import streamlit as st
import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

import base64

def centered_image(image_path, width=120):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()

    st.markdown(
        f"""
        <div style="display:flex; justify-content:center;">
            <img src="data:image/png;base64,{encoded}" width="{width}">
        </div>
        """,
        unsafe_allow_html=True
    )


st.set_page_config(
    page_title="Ventrix",
    page_icon="🚀",
    layout="wide"
)

#logo ---->


centered_image("logo.png", width=120)



#content part ---->
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e1117;
        background-image: radial-gradient(
            rgba(212, 175, 55, 0.08) 1.8px,
            transparent 1px
        );
        background-size: 40px 40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("""
<h1 style="text-align:center; font-weight:700;">
-Ventrix-
</h1>
<p style="text-align:center; color: #b0b0b0;">
AI-powered startup analysis & financial insights
</p>
<hr style="border:1px solid #2c2c2c;">
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

#Here we take some input ---->

st.subheader("📝 Startup Details")


#Let the user choose ---->
st.subheader("👤 Select User Type")

user_type = st.radio(
    "Who is this platform for?",
    ["Startup / Entrepreneur", "Artisan / Local Business"]
)

if user_type == "Startup / Entrepreneur":
    st.subheader("📝 Startup Details")
    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            vision = st.text_area("Startup Idea / Vision")
            audience = st.text_input("Target Audience")

        with col2:
            revenue = st.number_input("Monthly Revenue", min_value=0)
            cost = st.number_input("Monthly Cost", min_value=0)
            specifications = st.text_area(
        "🌱 Sustainability / Ethical Preferences",
        placeholder="e.g. eco-friendly, cruelty-free, vegan, sustainable packaging"
    )

elif user_type == "Artisan / Local Business":
    st.subheader("🎨 Artisan Details")

    with st.container():
        artisan_story = st.text_area(
            "Tell your story (background, craft, culture)",
            placeholder="Describe your journey, craft, and cultural background"
        )

        product_details = st.text_area(
            "Describe your products",
            placeholder="What do you make? Materials, uniqueness, usage, etc."
        )

        marketing_goals = st.text_area(
            "What do you want help with?",
            placeholder="e.g. online marketing, pricing, social media, visibility"
        )


if st.button("Analyze"):
    try:
            if user_type == "Startup / Entrepreneur":
                if not vision or not audience:
                    st.error("Please enter startup vision and target audience.")
                else:
                    st.info("Analyzing startup with AI... 🤖")
                prompt = f"""
You are a startup advisor. Analyze the following startup information and provide:

1. A short investor-ready pitch (3–5 lines)
2. Key strengths
3. Potential risks
4. Suggestions to improve the business approach

Startup details:
Vision: {vision}
Target Audience: {audience}
Monthly Revenue: {revenue}
Monthly Cost: {cost}
"""

                response = openai.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )
                result = response.choices[0].message.content
                st.success("Analysis Complete ✅")
                st.write(result)

    # Graphical & Pictorial Insights ---->

                st.subheader("📊 Financial Overview")

                profit = revenue - cost

    # Bar chart data 📊 ---->
                
                import pandas as pd
                import altair as alt

                chart_df = pd.DataFrame({
                    "Category": ["Revenue", "Cost"],
                    "Amount": [revenue, cost]
    })

                bar_chart = alt.Chart(chart_df).mark_bar(size=50).encode(
                x=alt.X("Category", title=None),
                y=alt.Y("Amount", title="Amount"),
                color=alt.Color("Category", legend=None)
    )

                st.altair_chart(bar_chart, use_container_width=True)

    # Profit / Loss display 📉 ---->
                
                if profit > 0:
                    st.success(f"💰 Estimated Monthly Profit: ₹{profit}")
                    st.info("The startup shows early signs of profitability based on current inputs.")
                elif profit == 0:
                    st.warning("⚖️ The startup is currently breaking even.")
                else:
                    st.error(f"📉 Estimated Monthly Loss: ₹{abs(profit)}")
                    st.info("Costs are higher than revenue. Cost optimization is recommended.")

    # Cost-heavy Factor Identification 💸 ---->

                st.subheader("💸 Cost-heavy Factors & Optimization Insights")

                cost_prompt = f"""
    The startup has the following financials:
    - Monthly Revenue: {revenue}
    - Monthly Cost: {cost}

    Identify:
    1. Possible cost-heavy areas in such a startup
    2. Suggestions to reduce or optimize these costs
    3. One key financial recommendation

    Respond in clear bullet points.
    """

                cost_response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": cost_prompt}],
                temperature=0.6
    )

                cost_insights = cost_response.choices[0].message.content
                st.write(cost_insights)
    # Sustainability & Ethical Consideration Analysis 🌱 ---->

                if specifications.strip():
                    st.subheader("🌱 Sustainability & Ethical Considerations")

                    sustainability_prompt = f"""
    The startup has the following sustainability and ethical preferences:
    {specifications}

    Provide:
    1. Practical ways the startup can implement these preferences
    2. Operational or sourcing changes required
    3. Packaging or branding suggestions (if applicable)
    4. One realistic challenge and how to overcome it

    Respond in clear, concise bullet points.
    """

                    sustainability_response = openai.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": sustainability_prompt}],
                    temperature=0.6
        )

                    sustainability_insights = sustainability_response.choices[0].message.content

                    with st.container():
                        st.write(sustainability_insights)
                
                elif not specifications.strip():
                    st.info("🌱 Add sustainability or ethical preferences to receive tailored recommendations.")



        
            elif user_type == "Artisan / Local Business":
                st.subheader("🧵 AI Support for Artisans")

                artisan_prompt = f"""
            You are a digital marketing and branding assistant for local artisans.

            Artisan background and story:
            {artisan_story}

            Product details:
            {product_details}

            Support needed:
            {marketing_goals}

            Provide:
            1. A refined artisan story suitable for online platforms
            2. Digital product descriptions
            3. Online marketing ideas (social media, platforms, outreach)
            4. Pricing and target audience suggestions
            5. Ways to improve online visibility

            Respond in clear bullet points.
            """

                artisan_response = openai.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": artisan_prompt}],
                    temperature=0.6
                )

                artisan_result = artisan_response.choices[0].message.content

                with st.container():
                    st.write(artisan_result)

    except Exception as e:
        st.error(f"AI request failed: {e}")



# --.--.--.-- THANK YOU --.--.--.--