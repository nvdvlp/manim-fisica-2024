from manim import *

class conceptoDeFuerza(Scene):
    def construct(self):
        config.set_font = ("Georgia")
        #titulo
        titulo = Text("Concepto de Fuerza").scale(1.5)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        #definición de fuerza
        definicion = Text(
            "Fuerza: Es la interacción que es capaz de modificar\n"
            "la velocidad de movimiento de un cuerpo y/o estructura."
            ).scale(0.7).move_to(UP)
        #forumla de fuerza MathTex
        formula = MathTex(r"F = m \cdot a").scale(1.5).next_to(definicion, DOWN, buff = 0.5)
        self.play(Write(definicion))
        self.wait(1)
        self.play(Write(formula))
        self.wait(2)
        self.play(FadeOut(definicion, formula))

        #ejemplo de fuerza

        #titulo del problema
        ejemplo = Text("Ejemplo").scale(1.5).to_edge(UP, buff=0.5).set_color(YELLOW).shift(DOWN * 0.5)
        self.play(Write(ejemplo))
        self.wait(1)

        #FIGURAS
        caja = Square(side_length = 2, color = RED)
        magnitud = Text("F = 10 N").scale(0.5)
        haciaLaDerecha = Text("hacia la derecha").scale(0.3)
        flecha = Arrow(LEFT, RIGHT, color = YELLOW)
        flecha.next_to(caja, LEFT)
        
        self.play(Create(caja), Create(flecha))
        self.play(Write(magnitud.next_to(flecha, UP)))
        self.play(Write(haciaLaDerecha.next_to(flecha, DOWN)))
        self.wait(1)

        #animacion de las FIGURAS
        animacionDeCaja = caja.animate.shift(RIGHT * 3).fade(1)
        animacionDeFlecha = flecha.animate.shift(RIGHT * 3).fade(1)
        animacionMagnitud = magnitud.animate.shift(RIGHT * 3).fade(1)
        animacionHaciaLaDerecha = haciaLaDerecha.animate.shift(RIGHT * 3).fade(1)
        self.wait(1)
        self.play(animacionDeCaja, animacionDeFlecha, animacionMagnitud, animacionHaciaLaDerecha, run_time = 3)

        #explicacion del problema
        explicacion = Text(
                            "Una fuerza neta aplicada a un objeto determina su dirección de movimiento y la cantidad de aceleración experimentada.\n"
                            "La flecha amarilla representa la fuerza neta aplicada, mostrando la dirección y la magnitud de la fuerza.\n" 
                            "La animacion muestra cómo el objeto se mueve hacia la derecha en respuesta a esta fuerza neta.\n"
                            "desapareciendo gradual de la flecha representa cómo la fuerza aplicada disminuye con el tiempo."
                            ).scale(0.4)
        explicacion.align_to(ORIGIN)
        self.play(Write(explicacion))
        self.wait(7)
        
class LeyesDeNewton(Scene):
    def construct(self):
        config.set_font = ("Georgia")
        #Titulo
        titulo = Text("Leyes de Newton").scale(1.5).to_edge(UP)
        definicion = Text("Las Leyes de Newton son tres principios fundamentales\n" 
                          "que describen el movimiento de los objetos y cómo interactuan con las fuerzas.\n" 
                          "Formuladas por issac Newton en el siglo XVII, estas leyes son la base de la mecanica clásica").next_to(titulo, DOWN).scale(0.5).align_to(ORIGIN)
        
        #Animacion
        issacNewton = ImageMobject("./img/newton.jpg")
        issacNewton.scale(1).next_to(definicion, DOWN)

        self.play(Write(titulo))
        self.wait(1)
        self.play(Write(definicion))
        self.wait(1)
        self.play(FadeIn(issacNewton))
        self.wait(7)
        self.play(FadeOut(titulo, definicion, issacNewton))

class PrimeraLey(Scene):
    def construct(self):
        config.set_font = ("Georgia")

        # Título
        titulo = Text("Primera Ley De Newton").scale(1.5).to_edge(UP)
        definicion = Text(
            " '' Un objeto en reposo permanece en reposo y un objeto en movimiento continúa en movimiento con velocidad constante\n"
            "a menos que una fuerza externa actúe sobre él ''.\n"
            "Esta ley introduce el concepto de inercia, que es la resistencia de un objeto a cambiar su estado de movimiento."
        ).scale(0.4).next_to(titulo, DOWN, buff=0.5).align_on_border(LEFT)
        
        self.play(Write(titulo))
        self.wait(1)
        self.play(Write(definicion))
        self.wait(5)

        # Animación del carrito de compras
        carritoCompras = ImageMobject("./img/shopping-cart-market-free-png.webp")
        carritoCompras.scale(0.5).next_to(definicion, DOWN, buff=1).to_edge(LEFT)
        flecha = Arrow(LEFT, RIGHT, color=YELLOW)
        flecha.next_to(carritoCompras, LEFT)

        self.play(FadeIn(carritoCompras), Create(flecha))
        self.wait(2)

        animacionflecha = flecha.animate.shift(RIGHT * 2).fade(1)
        animacioncarrito = carritoCompras.animate.shift(RIGHT * 10).fade(1)
        self.play(animacionflecha, animacioncarrito, run_time=5)
        self.wait(5)
        self.play(FadeOut(titulo, definicion))

        # Ejemplo práctico

        ejemploPractico = Text("Ejemplo Práctico").scale(1.5).to_edge(UP)
        self.play(Write(ejemploPractico))

        carro = ImageMobject("./img/passenger-car-isolated-on-white-600nw-2307569253-removebg-preview.png").scale(0.5).to_edge(LEFT)
        flecha = Arrow(LEFT, RIGHT, color=YELLOW)
        flecha.next_to(carro, LEFT)

        # Texto explicativo inicial
        textoConstante = Text(
            "El carro se desplaza a velocidad constante.\n"
            "No hay fuerzas externas significativas actuando sobre él."
        ).scale(0.4).next_to(carro, RIGHT, buff=0.5)

        self.play(FadeIn(carro), FadeIn(flecha))
        self.wait(1)
        self.play(Write(textoConstante))
        self.wait(5)

        animacionflecha = flecha.animate.shift(RIGHT * 2).fade(1)
        animacioncarro = carro.animate.shift(RIGHT * 6)
        animaciontexto = textoConstante.animate.shift(RIGHT * 6).fade(1)
        self.play(animacionflecha, animacioncarro, animaciontexto, run_time=5)
        self.wait(2)

        # Añadir el texto de desaceleración y la animación de frenado
        textoDesaceleracion = Text(
            "El conductor deja de acelerar y no aplica los frenos.\n"
            "El carro continúa moviéndose por inercia, pero se desacelera\ndebido a la fricción con el aire y el pavimento."
        ).scale(0.4)

        textoDesaceleracion.next_to(carro, DOWN, buff=0.5)
        self.play(Transform(textoConstante, textoDesaceleracion))
        
        # Animación de desaceleración
        animacionFrenado = carro.animate.shift(RIGHT * 2)
        animacionTexto = textoConstante.animate.shift(RIGHT * 2)
        self.play(animacionFrenado, animacionTexto, run_time=5)
        
        self.wait(2)
        self.play(FadeOut(carro, textoConstante, flecha))
        self.wait(4)
        self.play(FadeOut(carro), FadeOut(textoDesaceleracion), FadeOut(ejemploPractico))

        # aplicaciones

        aplicaciones = Text("Aplicaciones").scale(1.5).to_edge(UP)
        textoAplicaciones = Text("Algunas de sus aplicaciones son:").scale(0.5).next_to(aplicaciones, DOWN)
        self.play(Write(aplicaciones))
        self.wait(1)
        self.play(Write(textoAplicaciones))
        self.wait(1)

        cinturonesImg = ImageMobject("./img/5d9df7720ee694ff08349570-todo-sobre-el-cinturon-de-seguridad-importancia-consejos-y-falsos-mitos.jpg").scale(0.3)
        cinturonesTxt = Text("Los cinturones de seguridad son una aplicación directa de la Primera Ley de Newton.\n"
                                     "En caso de una colisión, el vehículo se detiene abruptamente, pero debido a la inercia,\n" 
                                     "los ocupantes tienden a seguir en movimiento a la misma velocidad que el vehículo antes del impacto.\n"
                                    ).scale(0.3).next_to(cinturonesImg, DOWN)
        
        self.play(FadeIn(cinturonesImg), FadeIn(cinturonesTxt))
        self.wait(7)
        self.play(FadeOut(cinturonesImg), FadeOut(cinturonesTxt))

        navegacionMaritimaImg = ImageMobject("./img/barco.jpg").scale(1.0)
        navegacionMaritimaTxt = Text("Los barcos y embarcaciones también tienen una gran inercia.\n" 
                                     "En aguas tranquilas, un barco se mantendrá en movimiento a velocidad constante\n" 
                                     "si no hay fuerzas externas significativas actuando sobre él, como la fricción del agua o el viento.\n" 
                                     "Los navegantes deben considerar esta inercia para maniobrar y detener la embarcación de manera segura.\n"
                                    ).scale(0.3).next_to(navegacionMaritimaImg, DOWN)
        
        self.play(FadeIn(navegacionMaritimaImg), FadeIn(navegacionMaritimaTxt))
        self.wait(7)
        self.play(FadeOut(navegacionMaritimaImg), FadeOut(navegacionMaritimaTxt))

        frenosImg = ImageMobject("./img/frenos-enbici-ciclismo.jpg").scale(0.3)
        frenosTxt = Text(" Una bicicleta se detendran debido a la fuerza de fricción proporcionada por los frenos.\n"
                                     "Sin embargo, el ciclista continuará moviéndose hacia adelante debido a la inercia,\n"
                                       "lo que puede hacer que se incline hacia adelante.\n"
                                    ).scale(0.3).next_to(frenosImg, DOWN)
        
        self.play(FadeIn(frenosImg), FadeIn(frenosTxt))
        self.wait(7)
        self.play(FadeOut(frenosImg), FadeOut(frenosTxt))

        #Expresada matematicamente
        explicacion = Text(
            "No tiene una fórmula específica, pero se puede expresar conceptualmente:"
        ).scale(0.5).to_edge(UP)
        formula = MathTex(r"\sum \vec{F} = 0 \implies \text{velocidad constante}")
        concepto = Text(
            "Esto significa que si la suma de las fuerzas que actúan\n"
            "sobre un objeto es 0 el objeto mantendrá su estado de movimiento,\n"
            "ya sea en reposo o en movimiento rectilíneo uniforme."
        ).scale(0.4)
        formula.next_to(titulo, DOWN, buff=0.5)
        concepto.align_to(formula, LEFT)
        concepto_center = concepto.get_center()
        concepto.shift((0, -concepto_center[1], 0))

        self.play(Write(explicacion), Write(formula), Write(concepto))
        self.wait(5)


class SegundaLey(Scene):
    def construct(self):
        config.set_font = ("Georgia")   
         # Título
        titulo = Text("Segunda Ley De Newton").scale(1.5).to_edge(UP)
        definicion = Text(
            " '' La aceleración de un objeto es directamente es proporcional\n"  
            " a la fuerza neta que actúa sobre él e inversamente proporcional a su masa.''.\n"
            " Matemáticamente, se expresa como F=m*a, donde F es la fuerza neta, m es la masa del objeto y a es la aceleración. "
        ).scale(0.4).next_to(titulo, DOWN, buff=0.5).align_on_border(LEFT)
        
        self.play(Write(titulo))
        self.wait(1)
        self.play(Write(definicion))
        self.wait(5)

        # Animación del carrito de compras
        carritoComprasLleno = ImageMobject("./img/png-clipart-shopping-cart-shopping-cart-removebg-preview.png")
        carritoComprasLleno.scale(1.0).next_to(definicion, DOWN, buff=1).to_edge(LEFT)
        flecha = Arrow(LEFT, RIGHT, color=YELLOW)
        flecha.next_to(carritoComprasLleno, LEFT)

        self.play(FadeIn(carritoComprasLleno), Create(flecha))
        self.wait(2)

        animacionflecha = flecha.animate.shift(RIGHT * 2).fade(1)
        animacioncarrito = carritoComprasLleno.animate.shift(RIGHT * 5).fade(1)
        self.play(animacionflecha, animacioncarrito, run_time=5)
        self.wait(5)
        self.wait(1)

        textoExplicativo = Text("El carrito de compras al tener objetos adentro\n" 
                                "su masa aumenta a 20kg y al ejercer 10 N esta,\n" 
                                "no llega acelerar de la misma forma.\n"
                                "F = m*a => 10N = 20kg * a => 20kg / 10N = 2m/s\n"
                                "El carrito se movilizoa 2m/s"
                                ).scale(0.4)
        self.play(Write(textoExplicativo))
        self.wait(8)
        self.play(FadeOut(titulo, definicion, textoExplicativo))

        # aplicaciones

        aplicaciones = Text("Aplicaciones").scale(1.5).to_edge(UP)
        textoAplicaciones = Text("Algunas de sus aplicaciones son:").scale(0.5).next_to(aplicaciones, DOWN)
        self.play(Write(aplicaciones))
        self.wait(1)
        self.play(Write(textoAplicaciones))
        self.wait(1)

        propulsionEspacialImg = ImageMobject("./img/propulsionEspacial.jpg").scale(1.5)
        propulsionEspacialTxt = Text("En la industria aeroespacial, la Segunda Ley de Newton\n"
                                     "es esencial para el diseño y operación de cohetes\n"
                                    "y otros vehículos espaciales.\n"
                                    "Los ingenieros deben calcular con precisión la fuerza\n"
                                    "necesaria para acelerar el vehículo y superar la gravedad\n" 
                                    "terrestre, así como también considerar la masa del vehículo y su carga útil."
                                    ).scale(0.3).next_to(propulsionEspacialImg, DOWN)
        
        self.play(FadeIn(propulsionEspacialImg), FadeIn(propulsionEspacialTxt))
        self.wait(7)
        self.play(FadeOut(propulsionEspacialImg), FadeOut(propulsionEspacialTxt))

        industriaAutomotrisImg = ImageMobject("./img/Industria-automotriz-1.jpg").scale(0.3)
        industriaAutomotrisTxt = Text("Las pruebas de seguridad de vehículos, como las pruebas de choque,\n" 
                                       "se basan en los principios de la Segunda Ley de Newton.\n"
                                        "Estas pruebas evalúan cómo los vehículos y sus ocupantes responderán a fuerzas externas\n"
                                        ", como las generadas durante una colisión, y ayudan a diseñar vehículos más seguros mediante\n" 
                                        "la incorporación de características como zonas de deformación controlada y sistemas de restricción."
                                    ).scale(0.3).next_to(industriaAutomotrisImg, DOWN)
        
        self.play(FadeIn(industriaAutomotrisImg), FadeIn(industriaAutomotrisTxt))
        self.wait(7)
        self.play(FadeOut(industriaAutomotrisImg), FadeOut(industriaAutomotrisTxt))

        equiposDeportivosImg = ImageMobject("./img/ciclismo.jpg").scale(1.5)
        equiposDeportivosTxt = Text("En deportes como el ciclismo, el diseño de bicicletas\n"
                                     "y cascos se basa en la aplicación de la Segunda Ley de Newton\n"
                                    "para optimizar la relación entre la masa y la fuerza necesaria\n"
                                    "para acelerar o detener el movimiento.\n"
                                    "Del mismo modo, en deportes de motor como el automovilismo y el ciclismo de velocidad, \n"
                                    "el diseño de vehículos y bicicletas se ajusta para maximizar la velocidad\n" 
                                    "y la eficiencia utilizando los principios de esta ley.\n"
                                    ).scale(0.3).next_to(propulsionEspacialImg, DOWN)
        
        self.play(FadeIn(equiposDeportivosImg), FadeIn(equiposDeportivosTxt))
        self.wait(7)
        self.play(FadeOut(equiposDeportivosImg), FadeOut(equiposDeportivosTxt))

class TerceraLey(Scene):
    def construct(self):        
        config.set_font = ("Georgia")   
         # Título
        titulo = Text("Tercera Ley De Newton").scale(1.5).to_edge(UP)
        definicion = Text(
            " '' Por cada acción, hay una reacción igual y opuesta.\n" 
            "Esto significa que si un objeto A ejerce una fuerza sobre un objeto B,\n" 
            "el objeto B ejerce una fuerza de igual magnitud pero en dirección opuesta sobre el objeto A. ''\n"
        ).scale(0.4).next_to(titulo, DOWN, buff=0.5).align_on_border(LEFT)
        
        self.play(Write(titulo))
        self.wait(1)
        self.play(Write(definicion))
        self.wait(5)

        # Animación del carrito de compras
        carritoComprasLleno = ImageMobject("./img/shopping-cart-market-free-png.webp")
        carritoComprasLleno.scale(0.5).next_to(definicion, DOWN, buff=1).to_edge(LEFT)
        
        flecha = Arrow(LEFT, RIGHT, color=YELLOW)
        flecha.next_to(carritoComprasLleno, LEFT)

        # Bloque en el suelo
        bloque = Square(side_length=1.0, color=BLUE, fill_opacity=1)
        bloque.next_to(carritoComprasLleno, RIGHT, buff=2.8)  # Ajustar buff para alinearlo

        self.play(FadeIn(carritoComprasLleno), Create(flecha), FadeIn(bloque))
        self.wait(2)

        # Animación de avance del carrito
        animacion_flecha = flecha.animate.shift(RIGHT * 3).fade(1)
        animacion_carrito = carritoComprasLleno.animate.shift(RIGHT * 3)
        self.play(animacion_flecha, animacion_carrito, run_time=3)
        self.wait(1)

        # Animación del choque y retroceso
        choque = Text("¡Choque!").set_color(RED).scale(1.2).next_to(carritoComprasLleno, UP)
        self.play(Write(choque))
        self.wait(1)
        retroceso_carrito = carritoComprasLleno.animate.shift(LEFT * 2)
        self.play(retroceso_carrito, FadeOut(choque), run_time=2)
        self.wait(1)

        # Texto explicativo
        textoExplicativo = Text(
            "La Tercera Ley de Newton establece que cuando el carrito choca\n" 
            "contra una superficie este tiende a generar una reacción opuesta y la fuerza es contraria"
        ).scale(0.4).move_to(ORIGIN)
        
        # Desaparecer todos los elementos
        self.play(FadeOut(carritoComprasLleno, bloque))
        self.wait(1)

        # Mostrar texto explicativo
        self.play(Write(textoExplicativo))
        self.wait(8)
        self.play(FadeOut(textoExplicativo, definicion, titulo))
        self.wait(1)
        
        # matematicamente
        matematicamente = Text("Matematicamente se puede representar de esta forma").scale(0.5).to_edge(UP)
        formula = MathTex(r"\vec{F}_{AB} = -\vec{F}_{BA}").scale(1.2).next_to(matematicamente, DOWN, buff=0.3)
        fab = MathTex(r"\vec{F}_{AB}").scale(0.2).next_to(formula, DOWN, buff=0.5).scale(3.2).to_edge(LEFT)
        fba = MathTex(r"\vec{F}_{BA}" ).scale(0.2).next_to(formula, DOWN, buff=0.5).scale(3.2).to_edge(LEFT).next_to(fab, DOWN)
        fabTxt = Text(": es la fuerza que el objeto A ejerce sobre el objeto B.").scale(0.5).next_to(fab, RIGHT)
        fbaTxt = Text(": es la fuerza que el objeto B ejerce sobre el objeto A.").scale(0.5).next_to(fab, RIGHT).next_to(fabTxt, DOWN)

        self.play(Write(matematicamente))
        self.wait(2)
        self.play(Write(formula))
        self.wait(1)
        self.play(Write(fab), Write(fabTxt))
        self.wait(1)
        self.play(Write(fba), Write(fbaTxt))
        self.wait(1)
