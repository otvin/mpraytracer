Converted the raytracer to using python multiprocessing module.  This required moving certain variables/objects into global scope so each thread would have access.