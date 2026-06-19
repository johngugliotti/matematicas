Changing a quadratic equation from **standard form** ($y = ax^2 + bx + c$) to **vertex form** ($y = a(x-h)^2 + k$) allows you to quickly identify the vertex of the parabola, which is located at the point $(h, k)$.

There are two primary methods to achieve this: **Completing the Square** (the traditional algebraic method) and **Using the Vertex Formula** (the quick shortcut).

---

### Method 1: Using the Vertex Formula (The Shortcut)

If you want to skip the algebraic heavy lifting, you can calculate the vertex coordinates $(h, k)$ directly using the coefficients from your original standard form equation ($a$, $b$, and $c$).

Using the same example: $y = 2x^2 + 12x + 16$, where **$a = 2$**, **$b = 12$**, and **$c = 16$**.

* **Step 1: Find $h$ using the formula $h = -\frac{b}{2a}$.**

$$h = -\frac{12}{2(2)} = -\frac{12}{4} = -3$$


* **Step 2: Find $k$ by plugging your $h$ value back into the original equation.**

$$k = 2(-3)^2 + 12(-3) + 16$$


$$k = 2(9) - 36 + 16$$


$$k = 18 - 36 + 16 = -2$$


* **Step 3: Substitute $a$, $h$, and $k$ into the vertex form template.**
The template is $y = a(x - h)^2 + k$. Substituting your values gives:

$$y = 2(x - (-3))^2 + (-2)$$


$$y = 2(x + 3)^2 - 2$$

The equation is now in vertex form, showing that the vertex is at $(-3, -2)$. Note that the sign inside the horizontal shift flips because the formula uses $(x - h)$.



---

### Method 2: Completing the Square

This is the standard algebraic approach. Let's walk through the steps using the example equation:

$$y = 2x^2 + 12x + 16$$

* **Step 1: Group the $x$ terms.** Separate the terms containing $x$ from the constant term.

$$y = (2x^2 + 12x) + 16$$


* **Step 2: Factor out the coefficient $a$.** If the $x^2$ term has a coefficient other than 1, factor it out from the grouped terms. In this case, $a = 2$.

$$y = 2(x^2 + 6x) + 16$$


* **Step 3: Find the value needed to complete the square.** Take the coefficient of the new linear $x$ term (which is 6), divide it by 2, and square the result.

$$\left(\frac{6}{2}\right)^2 = (3)^2 = 9$$


* **Step 4: Add and subtract this value to keep the equation balanced.** Add this number inside the parentheses to create a perfect square trinomial. Because that number is being multiplied by the outer coefficient $a$, you must subtract $a \times \text{value}$ outside the parentheses to keep the overall equation equal.

$$y = 2(x^2 + 6x + 9) + 16 - (2 \times 9)$$


$$y = 2(x^2 + 6x + 9) + 16 - 18$$


* **Step 5: Factor and simplify.** Collapse the perfect square trinomial into its squared binomial form, and combine the constants on the outside.

$$y = 2(x + 3)^2 - 2$$

The equation is now in vertex form, showing that the vertex is at $(-3, -2)$. Note that the sign inside the horizontal shift flips because the formula uses $(x - h)$.

---

### Quick Form Comparison

| Feature | Standard Form | Vertex Form |
| --- | --- | --- |
| **Equation** | $y = ax^2 + bx + c$ | $y = a(x-h)^2 + k$ |
| **Finding the Vertex** | Requires calculating $-\frac{b}{2a}$ | Directly visible as $(h, k)$ |
| **Y-Intercept** | Easily seen as $(0, c)$ | Requires setting $x = 0$ to solve |
| **Parabola Direction** | Determined by the sign of $a$ | Determined by the sign of $a$ |
