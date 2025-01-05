def ask_permission(resource_name):
    """Prompt the user for permission to access a resource."""
    response = input(f"This application needs permission to {resource_name}. Do you allow? (yes/no): ")
    return response.lower() == "yes"
