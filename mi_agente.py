"""
mi_agente.py — Aquí defines tu agente.
╔══════════════════════════════════════════════╗
║  ✏️  EDITA ESTE ARCHIVO                      ║
╚══════════════════════════════════════════════╝

Tu agente debe:
    1. Heredar de la clase Agente
    2. Implementar el método decidir(percepcion)
    3. Retornar: 'arriba', 'abajo', 'izquierda' o 'derecha'

Lo que recibes en 'percepcion':
───────────────────────────────
percepcion = {
    'posicion':       (3, 5),          # Tu fila y columna actual
    'arriba':         'libre',         # Qué hay arriba
    'abajo':          'pared',         # Qué hay abajo
    'izquierda':      'libre',         # Qué hay a la izquierda
    'derecha':        None,            # None = fuera del mapa

    # OPCIONAL — brújula hacia la meta.
    # No es percepción real del entorno, es información global.
    # Usarla hace el ejercicio más fácil. No usarla es más realista.
    'direccion_meta': ('abajo', 'derecha'),
}

Valores posibles de cada dirección:
    'libre'  → puedes moverte ahí
    'pared'  → bloqueado
    'meta'   → ¡la meta! ve hacia allá
    None     → borde del mapa, no puedes ir

Si tu agente retorna un movimiento inválido (hacia pared o
fuera del mapa), simplemente se queda en su lugar.
"""

from entorno import Agente


class MiAgente(Agente):
    """
    Tu agente de navegación.

    Implementa el método decidir() para que el agente
    llegue del punto A al punto B en el grid.
    """

    def __init__(self):
        super().__init__(nombre="Mi Agente")
        self.visitas = set()
        self.ultima_accion = None
        self.ACCIONES = ['arriba', 'abajo', 'izquierda', 'derecha']
        # Puedes agregar atributos aquí si los necesitas.
        # Ejemplo:
        #   self.pasos = 0
        #   self.memoria = {}

    def al_iniciar(self):
        """Se llama una vez al iniciar la simulación. Opcional."""
        pass

    def decidir(self, percepcion):
        
        """
        Decide la siguiente acción del agente.
        
        Parámetros:
            percepcion – diccionario con lo que el agente puede ver

        Retorna:
            'arriba', 'abajo', 'izquierda' o 'derecha'
        """
        # ╔══════════════════════════════════════╗
        # ║   ESCRIBE TU LÓGICA AQUÍ             ║
        # ╚══════════════════════════════════════╝

        # Ejemplo básico (bórralo y escribe tu propia lógica):
        #
        # vert, horiz = percepcion['direccion_meta']
        #
        # if percepcion[vert] == 'libre' or percepcion[vert] == 'meta':
        #     return vert
        # if percepcion[horiz] == 'libre' or percepcion[horiz] == 'meta':
        #     return horiz
        #
        # return 'abajo'

        pos = percepcion['posicion']
        self.visitas.add(pos)

        opuesto = {
            'arriba': 'abajo',
            'abajo': 'arriba',
            'izquierda': 'derecha',
            'derecha': 'izquierda'
        }

        for direccion in self.ACCIONES:
            if percepcion.get(direccion) == 'meta':
                self.ultima_accion = direccion
                return direccion

        vert, horiz = percepcion['direccion_meta']

        for direccion in [vert, horiz]:
            if percepcion.get(direccion) == 'libre':
                if self.ultima_accion is None or direccion != opuesto[self.ultima_accion]:
                    self.ultima_accion = direccion
                    return direccion

        for direccion in self.ACCIONES:
            if percepcion.get(direccion) == 'libre':
                if self.ultima_accion is None or direccion != opuesto[self.ultima_accion]:
                    self.ultima_accion = direccion
                    return direccion

        for direccion in self.ACCIONES:
            if percepcion.get(direccion) == 'libre':
                self.ultima_accion = direccion
                return direccion

        return 'abajo'