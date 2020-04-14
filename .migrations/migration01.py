''' Migrate to new database. '''

from configparser import ConfigParser

from sqlalchemy import create_engine
import pandas as pd

old_config_parser = ConfigParser()
old_config_parser.read('.old_db.config')

new_config_parser = ConfigParser()
new_config_parser.read('../.macecomp.config')

# Connect to old database
db_engine = create_engine(
    'mysql+mysqlconnector://{username}:{password}@{host}/{database}'.
    format(**old_config_parser['DATABASE OLD'])
)
con = db_engine.connect()

# Pull tables from old database
admin_df = pd.read_sql_table('ADMIN', con=con)
instructor_df = pd.read_sql_table('INSTRUCTOR', con=con)
student_df = pd.read_sql_table('STUDENT', con=con)

comp_df = pd.read_sql_table('COMP', con=con)

class_df = pd.read_sql_table('CLASS', con=con)

transcript_df = pd.read_sql_table('TRANSCRIPT', con=con)

four_q_df = pd.read_sql_table('4Q', con=con)
ten_q_df = pd.read_sql_table('10Q', con=con)

con.close()

# Connect to new database
db_engine = create_engine(
    'mysql+mysqlconnector://{username}:{password}@{host}/{database}'.
    format(**new_config_parser['DATABASE'])
)
con = db_engine.connect()

# Get structure of new user table
user_df = pd.read_sql_table('user', con=con)

# Insert students into user_df
for _, student in student_df.iterrows():
    row = {
        'user_id': student.student_id,
        'bb_user_id': student.bb_id,
        'first_name': student.first_name,
        'last_name': student.last_name,
        'role': 'STUDENT'
    }

    user_df = user_df.append(row, ignore_index=True)

# Insert instructors into user_df
for _, instructor in instructor_df.iterrows():
    row = {
        'user_id': instructor.instructor_id,
        'pre':  instructor.pre,
        'first_name': instructor.first_name,
        'last_name': instructor.last_name,
        'role': 'NONGRADING_INSTRUCTOR'
    }

    user_df = user_df.append(row, ignore_index=True)

# Insert admins into user_df
for _, admin in admin_df.iterrows():
    row = {
        'user_id': admin.admin_id,
        'email': admin.email,
        'role': 'ADMIN'
    }

    user_df = user_df.append(row, ignore_index=True)

user_df.sort_values(by='user_id', inplace=True)

# Get structure for new question table
question_df = pd.read_sql_table('question', con=con)

for _, comp in comp_df.iterrows():
    row = {
        'question_id': comp.comp_id,
        'bb_column_id': comp.bb_grade_column,
        'bb_content_id': comp.bb_content,
        'grading_istructor': comp.grading_instructor,
        'text': comp.question_text
    }

    question_df = question_df.append(row, ignore_index=True)

question_df.sort_values(by='question_id', inplace=True)

# Get structure for new course table
course_df = pd.read_sql_table('course', con=con)

for _, course in class_df.iterrows():
    row = {
        'course_id': course.class_id,
        'instructor_id': course.instructor_id,
        'question_id': course.comp_id,
        'year': course.yr_cde,
        'term': course.trm_cde,
        'course_code': course.crs_cde,
        'division': course.div
    }

    course_df = course_df.append(row, ignore_index=True)

print('All Done!')