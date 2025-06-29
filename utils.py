user_memory = {}

def set_user_name(user_id, name):
    user_memory[user_id] = name

def get_user_name(user_id):
    return user_memory.get(user_id, None)
