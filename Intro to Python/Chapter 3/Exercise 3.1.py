# fig03_03.py

# initialize variables

passes = 0 # number of passes
failures = 0 # number of failures

# process 10 students

for student in range(10):
    # get one exam result
    result = int(input('Enter result (1=pass, 2=fail): '))
   
    while 1 <= result <= 2:
        if result == 1:
            passes = passes + 1
            break
        elif result == 2:
            failures = failures + 1
            break
        else:
            continue
# termination phase

print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to Instructor')