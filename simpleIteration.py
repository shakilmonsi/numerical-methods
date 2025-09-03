# -----------------------------
# Simple Iteration Method in Python
# Equation rearranged: x = (2*x^2 + 3)/5
# ----------------------------- 

# Initial guess
x = 0   # শুরুতে x = 0 ধরা হলো

# Maximum 100 iterations
for iteration in range(1, 101):
    
    # Next iteration value বের করা হলো
    xnew = (2*x**2 + 3)/5   # x = g(x) = (2*x^2 + 3)/5

    # Convergence check
    if xnew == x:            # যদি নতুন value আগের value এর সমান হয়
        break                # loop থেকে বের হয়ে আসা

    # Update x for next iteration
    x = xnew

    # Current iteration value print করা হলো
    print('Iteration %d: x = %.6f' % (iteration, xnew))

# শেষ iteration বা convergence-এর পরে final value print
print('The root after iteration: %.6f' % x)
print('Total number of iterations: %d' % iteration)
