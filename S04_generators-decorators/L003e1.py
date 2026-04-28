def deployment_status():
    status = "PENDING"
    yield status
 
    status = "IN_PROGRESS"
    yield status
 
    status = "COMPLETED"
    print(f"Final state: {status}")
 
d_status = deployment_status()
print(f"1: {next(d_status)}")
print(f"2: {next(d_status)}")
try:
    next(d_status)
except StopIteration:
    print("3: Deployment finished.")