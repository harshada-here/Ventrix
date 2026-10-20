
import streamlit as st
import base64
import pandas as pd
import altair as alt


st.set_page_config(
    page_title="Ventrix",
    page_icon="🚀",
    layout="wide"
)


# ---------------- LOGO ----------------

def centered_image(image_path, width=120):
    try:
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()

        st.markdown(
            f"""
            <div style="display:flex; justify-content:center;">
                <img src="data:image/png;base64,{encoded}"
                     width="{width}">
            </div>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.markdown(
            "<h2 style='text-align:center'>🚀 Ventrix</h2>",
            unsafe_allow_html=True
        )


centered_image("logo.png", width=120)


# ---------------- DESIGN ----------------

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

st.markdown(
    """
    <h1 style="text-align:center; font-weight:700;">
        -Ventrix-
    </h1>
    <p style="text-align:center; color:#b0b0b0;">
        Startup analysis & financial insights
    </p>
    <hr style="border:1px solid #2c2c2c;">
    """,
    unsafe_allow_html=True
)

st.caption(
    "Ventrix provides input-based business insights "
    "using built-in recommendation rules."
)


# ---------------- STARTUP ANALYSIS ----------------

def analyze_startup(vision, audience, revenue, cost):
    profit = revenue - cost

    pitch = (
        f"{vision.strip()} is a business concept aimed at "
        f"{audience.strip()}. The business currently reports "
        f"₹{revenue:,.0f} in monthly revenue and "
        f"₹{cost:,.0f} in monthly costs. "
        "Its next priorities should be customer validation, "
        "cost management and sustainable growth."
    )

    strengths = [
        "The target audience is identified, providing a starting "
        "point for focused marketing.",
        "Tracking revenue and costs makes financial performance "
        "easier to evaluate.",
        "A clearly defined business idea helps guide product "
        "development and branding."
    ]

    risks = [
        "Actual customer demand may differ from initial assumptions.",
        "Unexpected expenses could reduce the available profit.",
        "Customer acquisition and competition may affect growth."
    ]

    improvements = [
        f"Interview potential customers in the {audience.strip()} "
        "segment to validate demand.",
        "Test the idea with a small launch before making large "
        "investments.",
        "Track sales, expenses and customer feedback every month.",
        "Set measurable short-term targets for customer growth "
        "and profitability."
    ]

    if profit < 0:
        improvements.insert(
            0,
            "Review recurring expenses and pricing because "
            "current monthly costs exceed revenue."
        )
    elif profit == 0:
        improvements.insert(
            0,
            "Work towards a positive operating margin by improving "
            "pricing, sales or cost efficiency."
        )
    else:
        improvements.insert(
            0,
            "Review the current profit margin and decide how much "
            "can safely be reinvested in growth."
        )

    return pitch, strengths, risks, improvements


def analyze_costs(revenue, cost):
    profit = revenue - cost

    if revenue > 0:
        cost_ratio = (cost / revenue) * 100
    else:
        cost_ratio = None

    insights = []

    if revenue == 0:
        insights.append(
            "No monthly revenue has been entered. Focus on "
            "validating demand and developing a realistic sales plan."
        )

    if cost > 0:
        insights.append(
            "Review major expense categories such as inventory, "
            "salaries, marketing, rent, shipping and software."
        )

    if cost_ratio is not None:
        if cost_ratio > 100:
            insights.append(
                f"Costs are {cost_ratio:.1f}% of revenue. "
                "Identify avoidable expenses and review pricing."
            )
        elif cost_ratio > 80:
            insights.append(
                f"Costs are {cost_ratio:.1f}% of revenue. "
                "Monitor expenses closely and look for efficiency gains."
            )
        else:
            insights.append(
                f"Costs are {cost_ratio:.1f}% of revenue. "
                "Continue tracking margins and allow for unexpected costs."
            )

    if profit > 0:
        insights.append(
            f"Current estimated monthly profit is ₹{profit:,.0f}. "
            "Consider maintaining a cash reserve before expanding."
        )
    elif profit == 0:
        insights.append(
            "The business is at break-even based on the values entered. "
            "Explore ways to increase sales or reduce costs."
        )
    else:
        insights.append(
            f"The estimated monthly shortfall is ₹{abs(profit):,.0f}. "
            "Review pricing, sales volume and essential versus "
            "non-essential spending."
        )

    return insights


def analyze_sustainability(preferences):
    text = preferences.lower()
    insights = []

    if any(word in text for word in ["packaging", "eco-friendly", "plastic"]):
        insights.extend([
            "Compare recyclable, reusable or lower-material packaging "
            "options for cost and suitability.",
            "Avoid making environmental claims unless they can be "
            "supported by evidence."
        ])

    if any(word in text for word in ["vegan", "cruelty-free", "ethical"]):
        insights.extend([
            "Document supplier policies and verify relevant product "
            "and sourcing claims.",
            "Communicate ethical commitments clearly and accurately "
            "to customers."
        ])

    if any(word in text for word in ["sustainable", "environment", "green"]):
        insights.extend([
            "Measure material use, waste and energy consumption "
            "to identify practical improvements.",
            "Start with changes that are affordable and can be "
            "maintained as the business grows."
        ])

    if not insights:
        insights.extend([
            "Choose sustainability actions that match the product "
            "and the business budget.",
            "Review suppliers, packaging and waste to identify "
            "practical improvements."
        ])

    insights.append(
        "Potential challenge: sustainable alternatives may cost more. "
        "Compare suppliers and test options on a small scale first."
    )

    return insights


def analyze_artisan(story, products, goals):
    story_text = story.strip()
    product_text = products.strip()
    goals_text = goals.strip()

    refined_story = (
        f"{story_text}\n\n"
        "Our work reflects a commitment to our craft, the quality "
        "of our products and the story behind their creation."
    )

    product_description = (
        f"{product_text}\n\n"
        "Highlight the product's materials, craftsmanship, intended "
        "use, care instructions and unique features. Include accurate "
        "measurements and customization details where relevant."
    )

    marketing_ideas = [
        "Share clear product photographs and short videos showing "
        "the making process.",
        "Tell the story behind the craft, materials and inspiration.",
        "Create a consistent social media schedule and include "
        "clear ordering instructions.",
        "Ask satisfied customers for feedback and permission to "
        "feature their reviews.",
        "Explore suitable online marketplaces, local exhibitions "
        "and collaborations."
    ]

    pricing_ideas = [
        "Calculate material, labour, packaging, delivery and platform "
        "costs before setting a selling price.",
        "Research comparable products without undervaluing the time "
        "and skill involved.",
        "Test products with a small customer group and collect feedback."
    ]

    visibility_ideas = [
        "Use descriptive product titles and relevant search terms.",
        "Include location and craft details where appropriate.",
        "Provide accurate prices, availability and delivery information."
    ]

    if goals_text:
        marketing_ideas.insert(
            0,
            f"Prioritize the requested support area: {goals_text}"
        )

    return (
        refined_story,
        product_description,
        marketing_ideas,
        pricing_ideas,
        visibility_ideas
    )


# ---------------- USER INPUT ----------------

st.subheader("👤 Select User Type")

user_type = st.radio(
    "Who is this platform for?",
    ["Startup / Entrepreneur", "Artisan / Local Business"]
)


# ---------------- STARTUP FORM ----------------

if user_type == "Startup / Entrepreneur":

    st.subheader("📝 Startup Details")

    col1, col2 = st.columns(2)

    with col1:
        vision = st.text_area("Startup Idea / Vision")
        audience = st.text_input("Target Audience")

    with col2:
        revenue = st.number_input(
            "Monthly Revenue (₹)",
            min_value=0.0,
            step=1000.0
        )

        cost = st.number_input(
            "Monthly Cost (₹)",
            min_value=0.0,
            step=1000.0
        )

        specifications = st.text_area(
            "🌱 Sustainability / Ethical Preferences",
            placeholder="e.g. eco-friendly, cruelty-free, "
                        "vegan, sustainable packaging"
        )


# ---------------- ARTISAN FORM ----------------

else:

    st.subheader("🎨 Artisan Details")

    artisan_story = st.text_area(
        "Tell your story (background, craft, culture)",
        placeholder="Describe your journey, craft and background"
    )

    product_details = st.text_area(
        "Describe your products",
        placeholder="What do you make? Materials, uniqueness, usage, etc."
    )

    marketing_goals = st.text_area(
        "What do you want help with?",
        placeholder="e.g. online marketing, pricing, visibility"
    )


# ---------------- ANALYZE BUTTON ----------------

if st.button("Analyze", type="primary"):

    if user_type == "Startup / Entrepreneur":

        if not vision.strip() or not audience.strip():
            st.error("Please enter the startup vision and target audience.")

        else:
            pitch, strengths, risks, improvements = analyze_startup(
                vision, audience, revenue, cost
            )

            st.success("Analysis Complete ✅")

            st.subheader("🚀 Investor-Ready Pitch")
            st.write(pitch)

            st.subheader("💪 Key Strengths")
            for item in strengths:
                st.markdown(f"- {item}")

            st.subheader("⚠️ Potential Risks")
            for item in risks:
                st.markdown(f"- {item}")

            st.subheader("📈 Recommendations")
            for item in improvements:
                st.markdown(f"- {item}")

            # Financial overview
            st.subheader("📊 Financial Overview")

            profit = revenue - cost

            chart_df = pd.DataFrame({
                "Category": ["Revenue", "Cost"],
                "Amount": [revenue, cost]
            })

            bar_chart = alt.Chart(chart_df).mark_bar(size=50).encode(
                x=alt.X("Category:N", title=None),
                y=alt.Y("Amount:Q", title="Amount (₹)"),
                color=alt.Color("Category:N", legend=None),
                tooltip=["Category", "Amount"]
            )

            st.altair_chart(bar_chart, use_container_width=True)

            if profit > 0:
                st.success(
                    f"💰 Estimated Monthly Profit: ₹{profit:,.2f}"
                )
                st.info(
                    "Revenue exceeds costs based on the values entered. "
                    "This estimate excludes any unreported expenses."
                )

            elif profit == 0:
                st.warning(
                    "⚖️ The business is currently at break-even."
                )

            else:
                st.error(
                    f"📉 Estimated Monthly Loss: ₹{abs(profit):,.2f}"
                )
                st.info(
                    "Costs exceed revenue. Review pricing, sales and "
                    "expenses before making expansion decisions."
                )

            # Cost insights
            st.subheader("💸 Cost & Optimization Insights")

            for item in analyze_costs(revenue, cost):
                st.markdown(f"- {item}")

            # Sustainability insights
            if specifications.strip():
                st.subheader("🌱 Sustainability & Ethical Considerations")

                for item in analyze_sustainability(specifications):
                    st.markdown(f"- {item}")

            else:
                st.info(
                    "🌱 Add sustainability or ethical preferences "
                    "to receive relevant recommendations."
                )

    # ---------------- ARTISAN ANALYSIS ----------------

    else:

        if not artisan_story.strip() or not product_details.strip():
            st.error(
                "Please enter your story and product details "
                "to generate an analysis."
            )

        else:
            (
                refined_story,
                product_description,
                marketing_ideas,
                pricing_ideas,
                visibility_ideas
            ) = analyze_artisan(
                artisan_story,
                product_details,
                marketing_goals
            )

            st.success("Artisan Analysis Complete ✅")

            st.subheader("🧵 Refined Artisan Story")
            st.write(refined_story)

            st.subheader("🛍️ Product Description")
            st.write(product_description)

            st.subheader("📱 Marketing Ideas")
            for item in marketing_ideas:
                st.markdown(f"- {item}")

            st.subheader("💰 Pricing Suggestions")
            for item in pricing_ideas:
                st.markdown(f"- {item}")

            st.subheader("🔎 Improving Online Visibility")
            for item in visibility_ideas:
                st.markdown(f"- {item}")


# ---------------- FOOTER ----------------

st.markdown("---")
st.caption(
    "Ventrix | Business planning support. "
    "Recommendations are general guidance, not financial advice."
)
