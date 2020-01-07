# Mesh_simplification_python
An implementation of mesh simplification algorithm ([1]) using python

System requirement: python 3.7, numpy, and argparse.

How to run the program:

You can run the program by:
python mesh_simplify.py -i [input file path] -o [output file path] -r [simplification ratio (0~1)] -t [threshold parameter]

For example, run:
python mesh_simplify.py -i models/dinosaur.obj -o dinosaur_simp_30_0.obj -r 0.3 -t 0

Please see Guide.pdf for a detailed introduction of the code.

[1] Garland, Michael, and Paul S. Heckbert. "Surface simplification using quadric error metrics." Proceedings of the 24th annual conference on Computer graphics and interactive techniques. ACM Press/Addison-Wesley Publishing Co., 1997.
