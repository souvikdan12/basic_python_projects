from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Name - Resume</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
            color: #333;
        }  
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1, h2 {
            color: #007bff;
        }
        .section {
            margin-bottom: 20px;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin-bottom: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Souvik Dan</h1>
            <p>Email: souvikdan925@gmail.com | Phone: 9204150780 | LinkedIn: linkedin.com/in/yourprofile | Location: Jaipur , Rajasthan</p>
        </header>
        
        <section class="section">
            <h2>Professional Summary</h2>
            <p>A brief summary of your professional background, skills, and career goals. For example: "Experienced software developer with a passion for creating efficient solutions. Skilled in Python, web development, and problem-solving."</p>
        </section>
        
        <section class="section">
            <h2>Work Experience</h2>
            <ul>
                <li><strong>Job Title</strong> - Company Name, City, State (Month Year - Month Year)<br>
                - Responsibility or achievement 1<br>
                - Responsibility or achievement 2</li>
                <li><strong>Job Title</strong> - Company Name, City, State (Month Year - Month Year)<br>
                - Responsibility or achievement 1<br>
                - Responsibility or achievement 2</li>
            </ul>
        </section>
        
        <section class="section">
            <h2>Education</h2>
            <ul>
                <li><strong>Degree</strong> - University Name, City, State (Year)<br>
                - Relevant coursework or honors</li>
            </ul>
        </section>
        
        <section class="section">
            <h2>Skills</h2>
            <ul>
                <li>Skill 1 (e.g., Python, JavaScript)</li>
                <li>Skill 2 (e.g., HTML/CSS, Data Analysis)</li>
                <li>Skill 3 (e.g., Project Management, Communication)</li>
            </ul>
        </section>
        
        <section class="section">
            <h2>Projects or Certifications</h2>
            <ul>
                <li><strong>Streamlit Dashboard</strong> Hands-on project demonstrating data visualization and interactivity using Streamlit.</li>
                <li><strong>Certification</strong> LinuxWorld informatics pvt. ltd. 2025</li>
            </ul>
        </section>
    </div>
</body>
</html>

    """

@app.route("/about")
def abouta():
    return """
    <h1>I am home page</h1>
    <h2>This is demo of about page</h2>
    """
    
if __name__=='__main__':
    app.run()