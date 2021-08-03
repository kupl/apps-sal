# Create a function args_count, that returns count of passed arguments
def args_count(*arbitrarios, **arbitrariosCla):
    return (len(arbitrarios) + len(arbitrariosCla))
