from flask import Flask,datetime 


my_incident= []

class Incident:

    records = [
        {
            "id" : 1,
            "location" : {"Lat": "", "Long": ""},
            "type": "red-flag",
            "created_on": "13/01/2019",
            "created_by": 1,
            "status": "draft",
            "images" : ["Image_1", "Image_2"],
            "videos" : ["Video_1", "Video_2"],
            "comment" : "This is draft comment"
        }
    ]
class user:
    users = [
        {
            "id": 1,
            "firstname": "logose",
            "lastname":  "mastula",
            "othername":  "mercy",
            "email":   "logosemastula@gmail.com",
            "phonenumber": "0752230290",
            "username": "mastu",
            "Isadmin":  "True"
            "registered": "14/01/2019"
        }
    ]
    def init (self, user_details):
        """ Initiallising user """
        self.firstname = user_details["firstname"]
        self.lastname = user_details["lastname"]
        self.othername= user_details["othername"]
        self.email =user_details["email"]
        self.phonenumber =user_details["phonenumber"]
        self.username = user_details["username"]
        self.Isadmin = user_details["Isadmin"]
        self.registered = datetime.now()

    def get_user_details(self):
        return
        {
        "id" = len(self.users)+1,
        "firstname": self.firstname
        "lastname": self.lastname,
        "othername": self.othername,
        "email": self.email,
        "phonenumber": self.phonenumber,
        "username": self.username,
        "Isadmin": self.Isadmin
        "registered": self.registered
        }
    def User_register(self,user):
        if user in users:
            self.users.append(user)
            return user
        else:
            return []

 


