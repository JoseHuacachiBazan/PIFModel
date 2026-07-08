# ================================
# Generar mapa 3D de concentración uniforme
# Formato: x y z concentración
# ================================

Nx = 250
Ny = 250
Nz = 250

C0 = 100.0  # concentración uniforme (CAMBIA ESTE VALOR)

output_file = "uniform_concentration_map.dat"

with open(output_file, "w") as f:
    for x in range(Nx):
        for y in range(Ny):
            for z in range(Nz):
                f.write(f"{x} {y} {z} {C0:.5f}\n")

print(f"Archivo '{output_file}' generado correctamente.")
