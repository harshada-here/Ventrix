# Ventrix
Ventrix: AI-powered startup analysis &amp; financial insights
🚀 Ventrix

(AI-Powered Startup & Artisan Insight Platform)

📌 Overview

Ventrix is an AI-driven web application designed to help startup founders and local artisans make informed business decisions.
The platform analyzes user inputs and generates actionable insights, financial visualizations, and practical recommendations using artificial intelligence.

It supports two user modes:

Startup / Entrepreneur

Artisan / Local Business

🎯 Problem Statement

Early-stage startups and local artisans often lack access to:

strategic business guidance

financial clarity

digital marketing insights

Ventrix AI bridges this gap by acting as an intelligent advisory assistant, providing structured insights in a simple, accessible way.

✨ Key Features
🔹 Startup / Entrepreneur Mode

AI-based startup feasibility analysis

Risk identification and improvement suggestions

Revenue vs cost visualization

Cost-heavy factor identification

Sustainability & ethical consideration analysis

🔹 Artisan / Local Business Mode

Refined artisan storytelling

Digital product description generation

Online marketing & visibility suggestions

Pricing and target audience guidance

🔹 General Features

Clean, dark-themed dashboard UI

Interactive charts and visual insights

Secure API key handling using environment variables

Deployed as a web application using Streamlit

🛠️ Tech Stack

Streamlit – Interactive web application framework

OpenAI API – AI-powered insight generation

Python – Core application logic

Altair / Pandas – Data handling and visualization

Streamlit Cloud – Deployment platform

🔧 Application Flow

User selects their role (Startup or Artisan)

Relevant details are collected through the UI

Inputs are processed via the OpenAI API

Financial metrics are calculated (for startups)

Insights and visualizations are displayed on a dashboard

🔐 Security

API keys are not hardcoded

Managed securely using:

Environment variables (local)

Streamlit Secrets (cloud deployment)

🚀 Deployment

The application is deployed using Streamlit Cloud and is publicly accessible via a web link.

To deploy manually:

Push the project to GitHub

Connect the repository to Streamlit Cloud

Add the OpenAI API key in Streamlit Secrets

Deploy the app

📁 Project Structure
├── app.py
├── requirements.txt
├── logo.png
└── README.md

🌱 Future Enhancements

Integration with real-time market data

Downloadable reports (PDF)

Advanced financial analytics

Support for additional user categories

👥 Team

Built as part of a hackathon project with a focus on:

real-world applicability

scalability

clean UI/UX

responsible AI usage

🏁 Conclusion

Ventrix AI demonstrates how AI can be used responsibly to empower startups and artisans by converting raw ideas and data into meaningful, actionable insights through a simple web interface.
