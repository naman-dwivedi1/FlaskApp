If you want to use this project just clone it using git clone
<br>
then make a virtual enviroment by
`python3 -m venv env`

then activate the virtual environment by
`. env/bin/activate`

then install flask, SQLAlchemy and PyMySQL by
`pip install flask`
`pip install flask flask-sqlalchemy`
`pip install pymysql`

then project is ready to work
<br>
You can add user by /addUser api of type POST and pass the json object in the body
<br>
User have following fields: id, firstname, lastname, email, password
<br>
You can fetch all users by /readAllUsers api of type GET
<br>
You can update the user by /updateUser/id api of type PUT and pass the json object in the body
<br>
You can update some information of the user by /updateSomeInfo/id api of type PATCH and pass the json object in the body
<br>
You can delete user by /deleteUser/id api of type DELETE

Initial Database
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/13f0de1a-3076-4df0-b30e-c1503cf5600c">

Adding Users
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/ab837443-91a5-40ce-8502-4b2f881bd783">
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/5eb82337-fd20-449c-bc8a-5418c303ebba">

Updated Database
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/7458a217-c34c-4536-b5f4-8c34f2638790">

Getting Users
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/6f7a51de-349b-41e9-ae9e-101c6a03dfc6">

Updating User

Put:
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/5d01fbf5-aa6d-454f-8dac-679c5352fe6e">

Updated Database
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/de2e8e29-5919-448f-a28e-4abe8a576a48">

Patch:
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/b95e519a-ef0d-4a69-b9cf-b61fa5771aae">

Updated Database
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/bb57ab8d-bced-43bf-b28b-403b3ab2edbc">

Deleting User
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/953f5e71-cdfd-4697-9ebe-11989a545266">

Updated Database
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/d7f734bd-68b5-442a-b8fd-0cd3691c4e2c">










