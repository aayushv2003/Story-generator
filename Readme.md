# Bedtime Story Generator using Multi-Stage LLM Evaluation

## Overview

This project is an AI-powered bedtime story generation system for children ages 5 to 10 built using `gpt-3.5-turbo`.

The system was designed with a strong focus on:
- child safety
- emotional warmth
- prompt engineering
- iterative LLM evaluation
- structured story generation
- moral and educational storytelling

Instead of using a simple single-prompt workflow, the application uses a **multi-stage LLM pipeline** consisting of:
1. Story Planning
2. Story Generation
3. LLM-Based Story Evaluation
4. Conditional Story Revision
5. Final Safety Validation

The goal is to generate calming, age-appropriate bedtime stories that teach positive values such as honesty, kindness, courage, and responsibility.

---

# Motivation

Bedtime stories for children should be:
- emotionally safe
- easy to understand
- comforting before sleep
- educational without being harsh
- engaging while remaining calming

This project explores how multiple LLM agents can work together to improve story quality through planning, evaluation, feedback, and revision loops.

---

# Features

- Multi-stage storytelling pipeline
- Story planner agent
- Story generation agent
- LLM judge/evaluator
- Conditional story revision loop
- Final safety checker
- Emotional safety constraints
- Automatic output saving
- Child-safe prompting
- Age-appropriate language generation

---

# System Architecture

```text
User Input
    ↓
Story Planner Agent
    ↓
Story Generator Agent
    ↓
LLM Judge Agent
    ↓
Score Evaluation
    ↓
If Score < 8
    ↙           ↘
Revise Story    Keep Story
    ↓
Final Safety Check
    ↓
Final Bedtime Story
    ↓
Saved to sample_output.txt
```

---

# Components

## 1. Story Planner Agent

The planner creates:
- title
- main character
- setting
- moral lesson
- emotional journey
- beginning / middle / ending

This improves story structure and coherence before story generation begins.

Example planner output:

```text
Title: Emma's Cookie Confession
Moral Lesson: Honesty is always the best policy
Emotional Journey: Guilt → Courage → Relief → Peace
```

---

## 2. Story Generator Agent

The storyteller generates the initial bedtime story using:
- the user request
- the structured story plan

The prompts enforce:
- calm bedtime tone
- simple vocabulary
- emotional reassurance
- positive endings
- non-violent and non-scary storytelling

---

## 3. LLM Judge Agent

The judge evaluates story quality using multiple dimensions:

- Age Appropriateness
- Bedtime Friendliness
- Emotional Warmth
- Clarity and Simplicity
- Creativity
- Safety
- Moral Lesson Quality

The judge returns:
- overall score
- strengths
- improvements
- recommendation

This creates an iterative feedback loop instead of accepting the first generated output blindly.

---

## 4. Conditional Story Revision

If the story score is below a threshold:
- the system automatically revises the story using judge feedback.

This simulates iterative refinement and improves:
- coherence
- emotional quality
- readability
- bedtime tone

---

## 5. Final Safety Checker

The final story undergoes an additional safety validation step.

The system checks for:
- scary content
- violence
- shame-based lessons
- harsh punishment
- emotionally distressing endings
- inappropriate language
- overly complex wording

This was added to emphasize safe and responsible AI storytelling for children.

---

# Prompting Strategy

The application uses specialized prompts for different agents.

## Story Planner Prompt
Focus:
- structure
- emotional arc
- moral lesson
- child-safe themes

## Story Generator Prompt
Focus:
- calming tone
- bedtime suitability
- emotional warmth
- simple vocabulary

## Judge Prompt
Focus:
- evaluation
- scoring
- structured feedback
- safety review

## Revision Prompt
Focus:
- improving weak areas
- avoiding preachy tone
- enhancing emotional comfort

---

# Example Prompt

```text
Write a bedtime story for ages 5 to 10 about honesty.
The main character should be a girl named Emma who sees the last cookie that her mom baked for her class party.
Emma secretly eats it, feels guilty, and learns that telling the truth is better than hiding a mistake.
The story should feel warm, calming, emotionally reassuring, and end with a peaceful bedtime moment.
```

---

# Example Output

The generated output includes:
- Story Plan
- Judge Feedback
- Final Safety Validation
- Final Bedtime Story

All outputs are automatically saved to:

```text
sample_output.txt
```

---

# Technologies Used

- Python
- OpenAI API
- GPT-3.5-Turbo

---

# Installation

## Clone Repository

```bash
git clone <repo_link>
cd bedtime-story-ai
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Set OpenAI API Key

## Windows PowerShell

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

## Mac/Linux

```bash
export OPENAI_API_KEY="your_api_key_here"
```

---

# Run Application

```bash
python main.py
```

---

# Project Structure

```text
bedtime-story-ai/
│
├── main.py
├── requirements.txt
├── README.md
├── sample_output.txt
└── .gitignore
```

---

# Design Decisions

## Why Multi-Stage Generation?

A single prompt often produces:
- inconsistent quality
- weak moral lessons
- poor emotional tone
- less controlled outputs

The multi-stage architecture improves:
- consistency
- structure
- safety
- emotional quality
- evaluation transparency

---

## Why an LLM Judge?

The assignment specifically requested:
- an LLM-based evaluation system.

The judge acts as:
- a quality reviewer
- a safety reviewer
- a readability evaluator
- a moral alignment checker

This allows the system to refine outputs iteratively.

---

## Why Safety Constraints?

Children's bedtime stories should avoid:
- fear
- emotional distress
- shame
- harsh punishment

The prompts and safety checker intentionally guide the model toward:
- emotional reassurance
- kindness
- warmth
- peaceful endings

---

# Future Improvements

If given more time, future improvements would include:

- Story memory across multiple nights
- Interactive story choices
- Voice narration using text-to-speech
- Emotion-adaptive storytelling
- Dynamic reading difficulty by age
- Persistent child profiles and preferences
- Multi-agent creativity enhancement
- Story illustration generation
- Long-term safety evaluation pipeline

---

# Author

Ayush Verma

MS Computer Science  
University of Texas at Arlington
