import random
import math

def generate_scene(filename, procname):
	f = open(filename, 'w')

	f.write('def {}():\n'.format(procname))
	f.write('    global GLOBALWORLD\n')
	f.write('    ground_material = Lambertian(Color(0.5, 0.5, 0.5))\n')
	f.write('    GLOBALWORLD.add(Sphere(Point3(0.0, -1000.0, 0.0), 1000.0, ground_material))\n')
	f.write('\n')

	for a in range(-9, 9):
		for b in range(-9, 9):
			choose_mat = random.random()
			x = a + (0.9 * random.random())
			y = 0.2
			z = b + (0.9 * random.random())
			if math.sqrt(((x - 4.0) * (x - 4.0)) + (z * z)) > 0.9:
				f.write('    center = Point3({}, {}, {})\n'.format(x, y, z))
				if choose_mat < 0.8:
					# diffuse
					r = random.random() * random.random()
					g = random.random() * random.random()
					b = random.random() * random.random()
					f.write('    albedo = Color({}, {}, {})\n'.format(r, g, b))
					f.write('    sphere_material = Lambertian(albedo)\n')
					f.write('    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))\n')
				elif choose_mat < 0.95:
					# metal
					r = random.uniform(0.5, 1.0) * random.uniform(0.5, 1.0)
					g = random.uniform(0.5, 1.0) * random.uniform(0.5, 1.0)
					b = random.uniform(0.5, 1.0) * random.uniform(0.5, 1.0)
					fuzz= random.uniform(0.0, 0.5)
					f.write('    albedo = Color({}, {}, {})\n'.format(r, g, b))
					f.write('    fuzz = {}\n'.format(fuzz))
					f.write('    sphere_material = Metal(albedo, fuzz)\n')
					f.write('    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))\n')
				else:
					# glass
					f.write('    sphere_material = Dielectric(1.5)\n')
					f.write('    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))\n')
				f.write('\n')

	f.write('\n')

	f.write('    big_glass_material = Dielectric(1.5)\n')
	f.write('    GLOBALWORLD.add(Sphere(Point3(0.0, 1.0, 0.0), 1.0, big_glass_material))\n')
	f.write('\n')
	f.write('    big_diffuse_material = Lambertian(Color(0.4, 0.2, 0.1))\n')
	f.write('    GLOBALWORLD.add(Sphere(Point3(-4.0, 1.0, 0.0), 1.0, big_diffuse_material))\n')
	f.write('\n')
	f.write('    big_metal_material = Metal(Color(0.7, 0.6, 0.5), 0.0)\n')
	f.write('    GLOBALWORLD.add(Sphere(Point3(4.0, 1.0, 0.0), 1.0, big_metal_material))\n')
	f.write('\n')

	f.close()

if __name__ == '__main__':
	generate_scene('scene1.gen', 'generate_fancymarbles')