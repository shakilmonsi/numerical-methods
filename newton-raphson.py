# -----------------------------
# Newton-Raphson Method in Python
# Equation: f(x) = x^2 - 2x - 9
# Derivative: f'(x) = 2x - 2
# -----------------------------

# Initial guess
x = 2   # শুরুতে x = 2 ধরা হলো

# Maximum 100 iterations
for iteration in range(1, 101):

    # Newton-Raphson formula: xnew = x - f(x)/f'(x)
    xnew = x - (x**2 - 2*x - 9)/(2*x - 2)

    # Convergence check: যদি change খুব ছোট হয়, তাহলে loop থামবে
    if abs(xnew - x) < 0.01:  
        break

    # Update x for next iteration
    x = xnew

    # Current iteration value print করা হলো
    print('Iteration %d: x = %.6f' % (iteration, xnew))

# শেষ iteration বা convergence-এর পরে final value print
print('The root after iteration: %.6f' % x)
print('Total number of iterations: %d' % iteration)
