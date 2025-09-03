# Initial interval set করা হলো
# x1 = 0       # Interval শুরু
# x2 = 1.2     # Interval শেষ

x1=0
x2=1.2

# Interval-এর প্রাথমিক function values বের করা হলো
y1 = 2*x1**2 - 5*x1 + 3   # f(x1) হিসাব
y2 = 2*x2**2 - 5*x2 + 3   # f(x2) হিসাব

# Root আছে কিনা চেক করা হলো
# যদি y1*y2 > 0 হয়, তাহলে দুই পাশেই একই Sign → Root নেই
if y1 * y2 > 0:
    print('No roots exist within given interval')
    exit()   # প্রোগ্রাম থামানো হলো

# Bisection loop শুরু (সর্বোচ্চ 100 বার iteration)
for i in range(1, 101):
    # Midpoint বের করা হলো
    xh = (x1 + x2)/2

    # Midpoint-এর function value বের করা হলো
    yh = 2*xh**2 - 5*xh + 3

    # x1-এর নতুন function value আবার হিসাব করা হলো
    y1 = 2*x1**2 - 5*x1 + 3

    # যদি x1-এর function value প্রায় শূন্য হয়, তাহলে loop থেকে বের হয়ে আসবো
    if abs(y1) < 1.0e-6:
        break

    # Sign check করে interval update করা হলো
    # যদি y1*yh < 0 → Root আছে x1 এবং xh এর মধ্যে
    elif y1 * yh < 0:
        x2 = xh   # x2 update
    else:
        x1 = xh   # নাহলে Root আছে xh এবং x2 এর মধ্যে → x1 update

# Root এবং Iteration সংখ্যা print করা হলো
print('The root: %.5f' % x1)
print('Number of bisections: %d' % i)
