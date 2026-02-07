from open_ai import OpenAI
client = OpenAI(api_key="your-api-key-here")

def analyse_email(email_content):
    prompt = f"""
        Extract the following information from the email:
        - Customer Name
        - Topic
        - Urgency (High, Medium, Low)
        - Summary
        
        Return JSON formatted as:

        Email
        {email_content}
        """
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ], 
        temperature=0
    )
    return response.choices[0].message.content