import datetime

class User:
  def __init__(self, user_id, name, email, password, cell_phone, company_name):
    self.user_id = user_id
    self.name = name
    self.email = email
    self.password = self.encrypt_password(password)
    self.cell_phone = cell_phone
    self.company_name = company_name
    self.registration_date = datetime.datetime.now()
    self.shopping_lists = {}
    self.order_history = []
    self.posts = []

  def __str__(self):
    return f"User {self.name}, Email: {self.email}"

  def encrypt_password(self, password):
    #placeholder for encryption
    return password
  
  def create_post():
    post_id = len(User.all.)