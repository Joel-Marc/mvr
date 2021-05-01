from subprocess import check_output
print(check_output(r'dir "C:\Users\joelm\Downloads\ENTERTAINMENT\MOVIES\test" /B ', shell=True).decode())
