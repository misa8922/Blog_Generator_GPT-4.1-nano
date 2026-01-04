from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

def generate_blog_post(topic, length):
    prompt = f"Write a detailed blog post about the following topic:\n\n{topic}\n\nThe blog post should be approximately {length} words long."
    
    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_completion_tokens=length * 2,  # Approximate token count for word count 1 word=0.75 tokens
        temperature=0.9,
        #top_p=1,  #another way to control diversity
        frequency_penalty=0,  #reduce repetitiveness 0 means no penalty and higher no more repetitiveness
        presence_penalty=0  #MORE TALK  about more things and not the same topic encouraged new topics 
    )
    print("API Response:", response)
    
    blog_post = response.choices[0].message.content
    print("Generated Blog Post:\n", blog_post)
    return blog_post

def main():
    topic=input('Enter the blog topic: ')
    length=int(input('Enter the length of the blog needed: '))
    answer=generate_blog_post(topic, length)
    print(answer)

main()