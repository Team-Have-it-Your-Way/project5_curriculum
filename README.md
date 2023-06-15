# Curriculum Logs Project (Team Have it Your Way)

Group project between with team members Keila Camarillo and Brian ONeil

## Project Description

* Using the dataset for curriculum website logs from CodeUp, Ms. Boss Person has multiple questions to be answered about the data prior to her meeting. Our team will acquire, prep, and explore the data using analysis to answer the questions. An email will be prepared and pushed to Ms. Boss Person explaining the answers to the questions along with an attached slide and repository link to summarize the findings.

## Project Goals

* Working as a team, acquire, prep, and explore the curriculum website logs to answer at least five questions as complete as possible.

* Craft an email answering Ms. Boss' questions in complete from the findings in data exploration.

* Create a slide summarizing the answers to the bosses questions found in data exploration.

* Other key drivers:
    * Answer the following questions:
    * 1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
    * 2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
    * 3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
    * 6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
    * 7. Which lessons are least accessed?

## Initial Thoughts

* We believe there is enough data to explore in the dataset to answer all of the questions.

## The Plan

* Acquire 

* Prepare the data using the following columns: 
    * features:
        * date
        * endpoint
        * user_id
        * cohort_id
        * source_ip
        * start_date
        * end_date
        * program_id
        * cohort_name

* Explore dataset to answer questions:
    * Answer the following questions:
    * 1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
    * 2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
    * 3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
    * 6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
    * 7. Which lessons are least accessed?

## Data Dictionary

| Feature     | Definition                                                                                                                     |
|-------------|--------------------------------------------------------------------------------------------------------------------------------|
| date        | the date and time a user accessed Codeup curriculum internet page                                                              |
| endpoint    | the page the user landed on in the curriculum                                                                                  |
| user_id     | the number assigned to a user by CodeUp (i.e. student, staff)                                                                  |
| cohort_id   | the number assigned to a cohort in a program by CodeUp                                                                         |
| source_ip   | internet protocol address, is a numerical label assigned to each device connected to a computer network that uses the Internet |
| start_date  | start_date of cohort                                                                                                           |
| end_date    | end_date of cohort                                                                                                             |
| cohort_name | the name of the cohort spelled                                                                                                 |

## Steps to Reproduce
1) Clone the the following repo: git@github.com:Team-Have-it-Your-Way/project5_curriculum.git in terminal
2) Download the following .txt file into cloned repository: https://drive.google.com/file/d/1dWwP_4vqETIS2oMALU2mH3F6QQh1m8CT/view?usp=sharing
3) Run final notebook

## Takeaways and Conclusions
* Q1: The most occurring and consistent lesson for WebDev 1.0 is 'javascript-i-introduction', with 232 hits. For WebDev 2.0, the most occuring and consistent lesson is also 'javascript-i-introduction', with over 7,000 hits across cohorts. For Data Science 3.0, the most consistent lesson is 'classification-overview', with over 1,400 hits across cohorts.
* Q2: WebDev 1.0 cohort 1.0 and 10 other cohorts had 0-14 occurrences for 'javascript-i intro' lesson. WebDev 2.0 cohort 135.0 and 18 other cohorts had 0-300 occurrences. Data Science 3.0 cohort 59 had 1109 occurrences for 'classification-overview' lesson while 4 other cohorts had 0-445.
* Q3: A total of 139 active students across 31 cohorts from years 2014 to 2020 did not access the curriculum. Specifically, 81 students were from web development 1.0, 54 from web development 2.0, and 4 from data science.
* Q6 & Q7: In Web Development 1.0, HTML-css was the most common lesson while Fundamentals was the least common. For Web Development 2.0, Spring was the most common lesson while Databases was the least common. In Data Science, Classification was the most common lesson while Storytelling was the least common.
