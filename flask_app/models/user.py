from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod #this is to show all the users
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL('cd_users').query_db(query)
        print(results)
        all_users = []
        for one_user in results:
            all_users.append(cls(one_user))
        return all_users

    @classmethod #this is actually adding the new user
    def create(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);'
        results = connectToMySQL('cd_users').query_db(query, data)
        print(results)
        return results
    
    @classmethod #this is to read one users info
    def get_one(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        results = connectToMySQL('cd_users').query_db(query, data)
        print(results)
        return cls(results[0])

    @classmethod #this is to delete user
    def delete(cls, data):
        query = 'DELETE FROM users WHERE id = %(id)s;'
        results = connectToMySQL('cd_users').query_db(query, data)
        print(results)
        return results

    @classmethod #this is to actually edit the user
    def update(cls, data):
        query = 'UPDATE users set first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;'
        results = connectToMySQL('cd_users').query_db(query, data)
        print(results)
        return results