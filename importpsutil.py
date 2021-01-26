import psutil
print(f"Memory :{psutil.virtual_memory()}")
print(f"users :{psutil.cpu_times()}")
print(f"boot :{psutil.boot_time()}")
print(f"cpu :{psutil.cpu_times()}")