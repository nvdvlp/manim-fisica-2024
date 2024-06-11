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
        self.wait(4)

        #FIGURAS
        caja = Square(side_length = 2, color = RED)
        magnitud = Text("F = 10 N").scale(0.5)
        haciaLaDerecha = Text("hacia la derecha").scale(0.3)
        flecha = Arrow(LEFT, RIGHT, color = YELLOW)
        flecha.next_to(caja, LEFT)
        
        self.play(Create(caja), Create(flecha))
        self.play(Write(magnitud.next_to(flecha, UP)))
        self.play(Write(haciaLaDerecha.next_to(flecha, DOWN)))
        self.wait(4)

        #animacion de las FIGURAS
        animacionDeCaja = caja.animate.shift(RIGHT * 3).fade(1)
        animacionDeFlecha = flecha.animate.shift(RIGHT * 3).fade(1)
        animacionMagnitud = magnitud.animate.shift(RIGHT * 3).fade(1)
        animacionHaciaLaDerecha = haciaLaDerecha.animate.shift(RIGHT * 3).fade(1)
        self.wait(4)
        self.play(animacionDeCaja, animacionDeFlecha, animacionMagnitud, animacionHaciaLaDerecha, run_time = 3)

        #explicacion del problema
        explicacion = Text(
                            "Una fuerza neta aplicada a un objeto determina su dirección de movimiento y la cantidad de aceleración experimentada.\n"
                            "La flecha amarilla representa la fuerza neta aplicada, mostrando la dirección y la magnitud de la fuerza.\n" 
                            "La animacion muestra cómo el objeto se mueve hacia la derecha en respuesta a esta fuerza neta.\n"
                            "desapareciendo gradual de la flecha representa cómo la fuerza aplicada disminuye con el tiempo."
                            ).scale(0.3)
        explicacion.align_to(ORIGIN)
        self.play(Write(explicacion))
        self.wait(10)
        
        #ejemplo Practico
        ejemploPractico = Text("Ejemplo practico").scale(1.5).to_edge(UP, buff=0.5).set_color(YELLOW).shift(DOWN * 0.5)
        problema = Text("Un automóvil cuya masa es de 600kg\n"
                         "acelera a razón de 1,2m/s, ¿Qué fuerza lo impulso?"
                         ).scale(0.5).next_to(ejemploPractico, DOWN)
        self.play(Write(ejemploPractico))
        self.wait(4)
        self.play(Write(problema))
        self.wait(4)
