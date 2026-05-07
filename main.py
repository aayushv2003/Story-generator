import os
import re
from openai import OpenAI

"""
If I had 2 more hours, I would add:
- Story memory across multiple nights
- Voice narration using text-to-speech
- Interactive story choices for children
- Adaptive reading difficulty by age
- Stronger safety checks for emotional distress, scary content, and age-inappropriate themes
"""

MODEL = "gpt-3.5-turbo"


def get_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not found.")

    return OpenAI(api_key=api_key)


def call_model(prompt: str, max_tokens=1200, temperature=0.5) -> str:
    client = get_client()

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature,
        )

        return response.choices[0].message.content

    except Exception as error:
        raise RuntimeError(f"OpenAI API call failed: {error}")


def create_story_plan(user_request: str) -> str:
    prompt = f"""
You are a children's bedtime story planner.

Create a simple story plan for a bedtime story for children ages 5 to 10.

User Request:
{user_request}

Return:
- Title
- Main character
- Setting
- Moral lesson
- Emotional journey
- Beginning
- Middle
- Ending

Important:
- Keep it gentle, calming, and age-appropriate.
- Avoid shame, fear, harsh punishment, violence, or scary content.
- Teach through kindness and reassurance.
"""

    return call_model(prompt, temperature=0.3)


def generate_story(user_request: str, story_plan: str) -> str:
    prompt = f"""
You are a warm and creative bedtime storyteller.

Write a bedtime story for children ages 5 to 10.

Requirements:
- Gentle and calming bedtime tone
- Simple vocabulary
- Positive emotional ending
- No scary, violent, or inappropriate content
- Avoid shame, fear, or harsh punishment
- Teach through kindness and reassurance
- Around 500-700 words
- Include dialogue naturally
- End with a calm bedtime moment
- Teach a clear positive moral lesson

User Request:
{user_request}

Story Plan:
{story_plan}
"""

    return call_model(prompt, temperature=0.7)


def judge_story(story: str) -> str:
    prompt = f"""
You are an expert LLM judge for children's bedtime stories.

Evaluate the story for children ages 5 to 10.

Return your evaluation in this exact format:

Overall Score: X/10

Age Appropriateness: X/10
Bedtime Friendliness: X/10
Emotional Warmth: X/10
Clarity and Simplicity: X/10
Creativity: X/10
Safety: X/10
Moral Lesson Quality: X/10

Strengths:
1.
2.
3.

Improvements:
1.
2.
3.

Final Recommendation:
...

Important safety checks:
- No scary or violent content
- No shame-based lesson
- No harsh punishment
- No emotionally distressing ending
- Language should be simple for ages 5 to 10

Story:
{story}
"""

    return call_model(prompt, temperature=0.2)


def extract_overall_score(feedback: str) -> float:
    match = re.search(r"Overall Score:\s*(\d+(?:\.\d+)?)\s*/\s*10", feedback)

    if match:
        return float(match.group(1))

    return 0.0


def revise_story(story: str, feedback: str) -> str:
    prompt = f"""
You are improving a bedtime story using judge feedback.

Original Story:
{story}

Judge Feedback:
{feedback}

Rewrite and improve the story.

Requirements:
- Keep it appropriate for ages 5 to 10
- Calm bedtime tone
- Emotional reassurance
- Clear moral lesson
- Warm and satisfying ending
- Simple language
- No scary content
- No shame, fear, or harsh punishment
- End with a peaceful bedtime moment
- Avoid sounding preachy

Return only the improved final story.
"""

    return call_model(prompt, temperature=0.6)


def final_safety_check(story: str) -> str:
    prompt = f"""
You are a safety reviewer for children's bedtime stories.

Check whether this final story is safe and appropriate for ages 5 to 10.

Return in this exact format:

Safety Verdict: PASS or FAIL

Reason:
...

Check for:
- scary content
- violence
- shame-based lesson
- harsh punishment
- inappropriate content
- confusing or overly complex language
- emotionally distressing ending

Story:
{story}
"""

    return call_model(prompt, temperature=0.1)


def save_output(story_plan, feedback, safety_result, final_story):
    with open("sample_output.txt", "w", encoding="utf-8") as file:

        file.write("================ STORY PLAN ================\n\n")
        file.write(story_plan + "\n\n")

        file.write("================ JUDGE FEEDBACK ================\n\n")
        file.write(feedback + "\n\n")

        file.write("================ FINAL SAFETY CHECK ================\n\n")
        file.write(safety_result + "\n\n")

        file.write("================ FINAL BEDTIME STORY ================\n\n")
        file.write(final_story + "\n")


def main():
    print("Welcome to the Bedtime Story Generator!\n")

    user_input = input("What kind of bedtime story would you like?\n\n")

    print("\nCreating story plan...\n")
    story_plan = create_story_plan(user_input)

    print("Generating story...\n")
    initial_story = generate_story(user_input, story_plan)

    print("Judging story quality...\n")
    feedback = judge_story(initial_story)

    score = extract_overall_score(feedback)

    if score < 8:
        print(f"Overall score was {score}/10, so improving story...\n")
        final_story = revise_story(initial_story, feedback)
    else:
        print(f"Overall score was {score}/10, so keeping original story...\n")
        final_story = initial_story

    print("Running final safety check...\n")
    safety_result = final_safety_check(final_story)

    save_output(
        story_plan,
        feedback,
        safety_result,
        final_story
    )

    print("\nOutput saved to sample_output.txt\n")

    print("\n================ STORY PLAN ================\n")
    print(story_plan)

    print("\n================ JUDGE FEEDBACK ================\n")
    print(feedback)

    print("\n================ FINAL SAFETY CHECK ================\n")
    print(safety_result)

    print("\n================ FINAL BEDTIME STORY ================\n")
    print(final_story)


if __name__ == "__main__":
    main()