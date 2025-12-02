from fp_wrapper import solve_system

def run_case(x1_0, x2_0, tol, max_iter, scale):
    print(f"\nCase: x1_0={x1_0}, x2_0={x2_0}, tol={tol}, max_iter={max_iter}, scale={scale}")
    x1, x2, iters = solve_system(x1_0, x2_0, tol=tol, max_iter=max_iter, scale=scale)
    print("  x1 =", x1)
    print("  x2 =", x2)
    print("  iterations =", iters)

def main():
    run_case(0.5, 0.5, tol=1e-6, max_iter=1000, scale=0.1)

    run_case(0.5, 0.5, tol=1e-6, max_iter=1000, scale=0.05)

    run_case(1.0, -1.0, tol=1e-5, max_iter=500, scale=0.2)

if __name__ == "__main__":
    main()
