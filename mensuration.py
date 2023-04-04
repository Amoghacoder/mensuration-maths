print("So you were down to Earth so bad that you have to use a calculator to calculate?")
print("I actually think you need a therapy..")
print("Anyways, you are already here. Then let's start. What do you want to do?")
# program starts from here.
# Ignore the variable names, I used them for my convenience.

print("Properties = 1, formula = 2, shapes solving = 3")
giga = int(input())

if giga == 1:
    print("")

elif giga == 2:
    print("*Note that you get only formulas in this section, if you want to solve please go to the solving section*")
    print("Which formulas?")
    print("2D = 1, 3D = 2")
    For = int(input())

    if For == 1:
        print("Which shape?")
        print("square = 1, rectangle = 2, triangle = 3, rhombus = 4, parallelogram = 5, trapezium = 6, circle = 7")
        w_sha = int(input())

        if w_sha == 1:
            print("The formulas of square:")
            print("Area = 1, Perimeter = 2")
            f_squa = int(input())

            if f_squa == 1:
                print("The area of square is", "a x a")

            elif f_squa == 2:
                print("The perimeter of square is", "4a")

        elif w_sha == 2:
            print("The formulas of rectangle:")
            print("Area = 1, perimeter = 2")
            f_rec = int(input())

            if f_rec == 1:
                print("The area of rectangle is", "l x b")

            elif f_rec == 2:
                print("The perimeter of rectangle is", "2(l + b)")

        elif w_sha == 3:
            print("The formulas of triangle:")
            print("Area = 1, Perimeter = 2")
            f_tri = int(input())

            if f_tri == 1:
                print("The area of triangle is", "1/2 x b x h ")

            elif f_tri == 2:
                print("In perimeter we can calculate in two types")
                print("IF the triangle is equilateral then we can directly use", "3a", "as the formula.")
                print("BUT, we can use the general form of", "ab + bc + ca", "also.")

        elif w_sha == 4:
            print("The formulas of rhombus:")
            print("Area = 1, perimeter = 2")
            f_rho = int(input())

            if f_rho == 1:
                print("The area of rhombus is", "1/2 x d(1) x d(2)")

            elif f_rho == 2:
                print("The perimeter of rhombus is", "4a")
        elif w_sha == 5:
            print("The formulas of parallelogram:")
            print("Area = 1, perimeter = 2")
            f_para = int(input())

            if f_para == 1:
                print("The area of parallelogram is", "b x h")

            elif f_para == 2:
                print("The perimeter of parallelogram is", "2(l + b)")
        elif w_sha == 6:
            print("The formulas of trapezium:")
            print("Area = 1, perimeter = 2")
            f_tra = int(input())

            if f_tra == 1:
                print("Area of trapezium is", "1/2 x h x (a +b)")

            elif f_tra == 2:
                print("Perimeter of trapezium is the sum of all sides, or (ab + bc + cd + da)")
        elif w_sha == 7:
            print("The formulas of circle:")
            print("Area = 1, perimeter = 2")
            f_cir = int(input())

            if f_cir == 1:
                print("The area of circle is ", "π x r x r")

            elif f_cir == 2:
                print("The perimeter or circumference of circle is", "2πr")
    elif For == 2:
        print("Which type of formula?")
        print("LSA = 1, TSA = 2, Volume = 3")
        mad = int(input())

        if mad == 1:
            print("Which 3D shape?")
            print("Cube = 1, Cuboid = 2, Cylinder = 3, Cone = 4")
            w_3_sha = int(input())

            if w_3_sha == 1:
                print("Lateral surface area of a cube is", "4 x a x a")

            elif w_3_sha == 2:
                print("Lateral surface area of a cuboid is", "2 x h x (l + b)")

            elif w_3_sha == 3:
                print("Lateral surface area of a cylinder is", "2πrh")

            elif w_3_sha == 4:
                print("Lateral surface area of a cone is", "πrl")

        if mad == 2:
            print("Which 3D shape?")
            print("Cube = 1, Cuboid = 2, Cylinder = 3, Cone = 4")
            w_3_sha = int(input())

            if w_3_sha == 1:
                print("Total surface area of a cube is", "6 x a x a")

            elif w_3_sha == 2:
                print("Total surface area of a cuboid is", "2 x (l x h) + (b x h) + (h x l))")

            elif w_3_sha == 3:
                print("Total surface area of a cylinder is", "2 x π x r x (r + h)")

            elif w_3_sha == 4:
                print("Total surface area of a cone is", "2 x π x r x (r + l)")

        if mad == 3:
            print("Which 3D shape?")
            print("Cube = 1, Cuboid = 2, Cylinder = 3, Cone = 4")
            w_3_sha = int(input())

            if w_3_sha == 1:
                print("The volume of a cube is", "a x a x a")

            elif w_3_sha == 2:
                print("The volume of a cuboid is", "l x b x h")

            elif w_3_sha == 3:
                print("The volume of a cylinder is", "π x r x r x h")

            elif w_3_sha == 4:
                print("The volume of a cone is", "1/3(π x r x r x h)")

elif giga == 3:
    print("*Note that the formulas will be not shown during the solve if you want the formulas please choose*")
    print("*the formula section next time.*")
    print("Which dimension?")
    print("2D - 1, 3D - 2")
    shapes = int(input())

    if shapes == 1:
        print("Which shape?")
        print("square = 1, rectangle = 2, triangle = 3, parallelogram = 4, trapezium = 5, circle = 6, rhombus = 7")
        The_ultimate_variable = int(input())

        if The_ultimate_variable == 1:
            print("Calculate about the square")
            print("Area = 1, perimeter = 2")
            input1 = int(input())

            if input1 == 1:
                print("Enter the measure of one side of the square:")
                a = int(input())
                area = a**2
                print("Enter the unit of measurement:")
                unit1 = input()
                print("The area is", area, "sq.", unit1)

            elif input1 == 2:
                print("Enter the measure of one side of the square")
                a = int(input())
                p_of_square = 4 * a
                print("Enter the unit of measurement:")
                unit1 = input()
                print("The perimeter is", p_of_square, unit1)

        elif The_ultimate_variable == 2:
            print("Calculate about the rectangle")
            print("Area = 1, perimeter = 2")
            input2 = int(input())

            if input2 == 1:
                print("Enter the length of the rectangle:")
                length = float(input())
                print("Enter the breadth of the rectangle:")
                breadth = float(input())
                area_rectangle = length*breadth
                print("Enter the unit of measurement:")
                unit2 = input()
                print("The area of rectangle is", area_rectangle, "sq.", unit2)

            elif input2 == 2:
                print("Enter the length of the rectangle:")
                l = float(input())
                print("Enter the breadth of the rectangle:")
                b = float(input())
                p_rectangle = 2*(l + b)
                print("Enter the unit of measurement:")
                unit2 = input()
                print("The perimeter of the rectangle is", p_rectangle, unit2)

        elif The_ultimate_variable == 3:
            print("Calculate about the triangle")
            print("Area = 1, Perimeter = 2")
            input3 = int(input())

            if input3 == 1:
                print("Enter the base of the triangle:")
                base = int(input())
                print("Enter the height of the triangle:")
                h_triangle = int(input())
                a_triangle = 1/2 * (base * h_triangle)
                print("Enter the unit of measurement")
                unit3 = input()
                print("The area of triangle is", a_triangle, "sq.", unit3)

            if input3 == 2:
                print("Enter the first side:")
                a_side = int(input())
                print("Enter the second side:")
                b_side = int(input())
                print("Enter the third side:")
                c_side = int(input())
                p_triangle = a_side + b_side + c_side
                print("Enter the unit of measurement:")
                unit4 = input()
                print("The perimeter of the triangle is", p_triangle, unit4)

        elif The_ultimate_variable == 4:
            print("Calculate about the parallelogram")
            print("Area = 1, perimeter = 2")
            pramec = int(input())

            if pramec == 1:
                print("Enter the height of the parallelogram:")
                h_para = int(input())
                print("Enter the measure of the base of the parallelogram:")
                b_para = int(input())
                print("Enter the unit of measurement:")
                unit_para = input()
                print("The area of your parallelogram is", h_para * b_para, "sq.", unit_para)

            elif pramec == 2:
                print("Enter the length of the parallelogram:")
                l_para = int(input())
                print("Enter the breadth of the parallelogram:")
                b_para = int(input())
                print("Enter the unit of measurement:")
                u2_para = input()
                print("The perimeter of your parallelogram is", 2*(l_para + b_para), "sq.", u2_para)

        elif The_ultimate_variable == 5:
            print("Calculate about the trapezium:")
            print("Area = 1, perimeter = 2")
            traps = int(input())

            if traps == 1:
                print("Enter the height of the trapezium:")
                h_trap = int(input())
                print("Enter the measure of the first parallel side:")
                ps_1 = int(input())
                print("Enter the measure of the second parallel side:")
                ps_2 = int(input())
                print("Enter the unit of measurement:")
                u_trap = input()
                trap_area = 1/2 * h_trap * (ps_1 + ps_2)
                print("The area of your trapezium is", trap_area,  "sq.", u_trap)

            elif traps == 2:
                print("Enter the measure of the first side:")
                fs_trap = int(input())
                print("Enter the measure of the second side:")
                ss_trap = int(input())
                print("Enter the measure of the third side:")
                ts_trap = int(input())
                print("Enter the measure of the fourth side:")
                fourth_s_trap = int(input())
                print("Enter the unit of measurement:")
                u_trap = input()
                trap_per = fs_trap + ss_trap + ts_trap + fourth_s_trap
                print("The perimeter of your trapezium is", trap_per, "u_trap")

        elif The_ultimate_variable == 6:
            print("Calculate about the circle:")
            print("Area = 1, circumference(perimeter) = 2")
            circs = int(input())

            if circs == 1:
                print("Enter the measure of the radius:")
                r_circle = int(input())
                print("Enter the unit of measurement:")
                u_circle = input()
                a_circle = 22/7 * r_circle * r_circle
                print("The area of your circle is", a_circle, u_circle, "sq.")

            elif circs == 2:
                print("Enter the measure of the radius:")
                r_circle = int(input())
                print("Enter the unit of measurement:")
                u_circle = input()
                cir = 2 * 22/7 * r_circle
                print("The circumference of your circle is", cir, u_circle)

        elif The_ultimate_variable == 7:
            print("Calculate about the rhombus:")
            print("Area = 1, perimeter = 2")
            rhom = int(input())

            if rhom == 1:
                print("Enter the measure of the first diagonal:")
                d1 = int(input())
                print("Enter the measure of the second diagonal:")
                d2 = int(input())
                print("Enter the unit of measurement:")
                u_rhom = input()
                area_rhom = 1/2 * d1 * d2
                print("The area of your rhombus is", area_rhom, u_rhom, "sq.")

            elif rhom == 2:
                print("Enter the measure of a side:")
                s1 = int(input())
                print("Enter the unit of measurement:")
                u_rhom = input()
                peri_rhom = 4 * s1
                print("The perimeter of your rhombus is", peri_rhom, u_rhom, "sq.")

    elif shapes == 2:
        print("Which type of solving in 3D shapes?")
        print("LSA = 1, TSA = 2, Volume = 3")
        dim_3 = int(input())

        if dim_3 == 1:
            print("Which 3D shape?")
            print("Cube = 1, Cuboid = 2, Cylinder = 3, Cone = 4")
            dim_sha = int(input())

            if dim_sha == 1:
                print("Enter the measure of one side:")
                a_cube = int(input())
                print("Enter the unit of measurement:")
                u_cube = input()
                lsa_cube = 4 * a_cube * a_cube
                print("Lateral surface area of your cube is", lsa_cube, u_cube, "sq.")

            elif dim_sha == 2:
                print("Enter the height of the cuboid:")
                h_cuboid = int(input())
                print("Enter the length of the cuboid:")
                l_cuboid = int(input())
                print("Enter the breadth of the cuboid:")
                b_cuboid = int(input())
                print("Enter the unit of measurement:")
                u_cuboid = input()
                lsa_cuboid = 2 * h_cuboid * (l_cuboid + b_cuboid)
                print("Lateral surface area of your cuboid is", lsa_cuboid, u_cuboid, "sq.")

            elif dim_sha == 3:
                print("Enter the radius of the base:")
                r_base_cylinder = int(input())
                print("Enter the height of the cylinder:")
                h_cylinder = int(input())
                print("Enter the unit of measurement:")
                u_cylinder = input()
                lsa_cylinder = 2 * 22/7 * r_base_cylinder * h_cylinder
                print("Lateral surface area of your cylinder is", lsa_cylinder, u_cylinder, "sq.")

            elif dim_sha == 4:
                print("Enter the radius of the base:")
                r_base_cone = int(input())
                print("Enter the length of the cone:")
                l_cone = int(input())
                print("Enter the unit of measurement:")
                u_cone = input()
                lsa_cone = 22/7 * r_base_cone * l_cone
                print("Lateral surface area of your cone is", lsa_cone, u_cone, "sq.")

        elif dim_3 == 2:
            print("Which shape?")
            print("Cube = 1, Cuboid = 2, Cylinder = 3, Cone = 4")
            tsa_sha = int(input())

            if tsa_sha == 1:
                print("Enter the measure of one side:")
                s1_cube = int(input())
                print("Enter the unit of measurement:")
                u_cube = input()
                tsa_cube = 6 * s1_cube * s1_cube
                print("Total surface area of your cube is", tsa_cube, u_cube, "sq.")

            elif tsa_sha == 2:
                print("Enter the length of the cuboid:")
                l_cuboid = int(input())
                print("Enter the breadth of the cuboid:")
                b_cuboid = int(input())
                print("Enter the height of the cuboid:")
                h_cuboid = int(input())
                print("Enter the unit of measurement:")
                u_cuboid = input()
                tsa_cuboid = 2 * (l_cuboid * b_cuboid + b_cuboid * h_cuboid + h_cuboid * l_cuboid)
                print("Total surface area of your cuboid is", tsa_cuboid, u_cuboid, "sq.")

            elif tsa_sha == 3:
                print("Enter the radius of the base of the cylinder:")
                r_base_cylinder = int(input())
                print("Enter the height of the cylinder:")
                h_cylinder = int(input())
                print("Enter the unit of measurement:")
                u_cylinder = input()
                tsa_cylinder = 2 * 22/7 * r_base_cylinder * (r_base_cylinder + h_cylinder)
                print("Total surface area of your cylinder is", tsa_cylinder, u_cylinder, "sq.")

            elif tsa_sha == 4:
                print("Enter the radius of the base of the cone:")
                r_base_cone = int(input())
                print("Enter the length of the cone:")
                l_cone = int(input())
                print("Enter the unit of measurement:")
                u_cone = input()
                tsa_cone = 2 * 22/7 * r_base_cone * (r_base_cone + l_cone)
                print("Total surface area of your cone is", tsa_cone, u_cone, "sq.")

        elif dim_3 == 3:
            print("Which shape?")
            print("Cube = 1, Cuboid = 2, Cylinder = 3, Cone = 4")
            v_sha = int(input())

            if v_sha == 1:
                print("Enter the measure of one side:")
                s1_cube = int(input())
                print("Enter the unit of measurement:")
                u_cube = input()
                v_cube = s1_cube * s1_cube * s1_cube
                print("Volume of your cube is", v_cube, u_cube, "cube.")

            elif v_sha == 2:
                print("Enter the length of the cuboid:")
                l_cuboid = int(input())
                print("Enter the breadth of the cuboid:")
                b_cuboid = int(input())
                print("Enter the height of the cuboid:")
                h_cuboid = int(input())
                print("Enter the unit of measurement:")
                u_cuboid = input()
                v_cuboid = l_cuboid * b_cuboid * h_cuboid
                print("Volume of your cuboid is", v_cuboid, u_cuboid, "cube.")

            elif v_sha == 3:
                print("Enter the radius of the base of the cylinder:")
                r_base_cylinder = int(input())
                print("Enter the height of the cylinder:")
                h_cylinder = int(input())
                print("Enter the unit of measurement:")
                u_cylinder = input()
                v_cylinder = 22/7 * r_base_cylinder * r_base_cylinder * h_cylinder
                print("Volume of your cylinder is", v_cylinder, u_cylinder, "cube.")

            elif v_sha == 4:
                print("Enter the radius of the base of the cone:")
                r_base_cone = int(input())
                print("Enter the height of the cone:")
                h_cone = int(input())
                print("Enter the unit of measurement:")
                u_cone = input()
                v_cone = 22 / 7 * r_base_cone * r_base_cone * h_cone
                print("Volume of your cone is", v_cone, u_cone, "cube.")


else:
    print("Invalid input.")
