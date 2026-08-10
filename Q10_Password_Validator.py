def validate_password(password):
    errors = []
    
    if len(password) < 8:
        errors.append("Minimum 8 characters required")
    if not any(c.isupper() for c in password):
        errors.append("At least one uppercase letter required")
    if not any(c.islower() for c in password):
        errors.append("At least one lowercase letter required")
    if not any(c.isdigit() for c in password):
        errors.append("At least one digit required")
    if not any(c in "!@#$%^&*" for c in password):
        errors.append("At least one special character required")
    
    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }


#case 1: 'weak'
result1 = validate_password("weak")
print(f"'weak' -> is_valid: {result1['is_valid']} ({len(result1['errors'])} errors)")

#case 2: 'Weak123'
result2 = validate_password("Weak123")
print(f"'Weak123' -> is_valid: {result2['is_valid']} (no special char)")

#case 3: 'MySecure@1'
result3 = validate_password("MySecure@1")
print(f"'MySecure@1' -> is_valid: {result3['is_valid']} (no errors)")



