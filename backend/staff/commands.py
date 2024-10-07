from .models import AuthCode


def send_auth_code(email, name, code):
    # TODO: Send email with code to user
    pass


def generate_auth_code(email, name=None):
    code = AuthCode.generate_unique_code()
    AuthCode.objects.create(code=code)

    try:
        send_auth_code(email, name, code)
        # TODO: Remove this print statement
        print("Generated code: ", code)
        return code
    except Exception as e:
        print(f"Failed to send code to {email}: {e}")
