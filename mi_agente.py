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
        self.visitados = set()
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
        self.visitados.add(pos)

        # 1. Si la meta está al lado → ir directo
        for direccion in self.ACCIONES:
            if percepcion[direccion] == 'meta':
                return direccion

        # 2. Usar direccion_meta (brújula)
        vert, horiz = percepcion['direccion_meta']

        if vert != 'ninguna':
            if percepcion[vert] == 'libre':
                return vert

        if horiz != 'ninguna':
            if percepcion[horiz] == 'libre':
                return horiz

        # 3. Evitar repetir posiciones
        for direccion in self.ACCIONES:
            if percepcion[direccion] == 'libre':
                nueva_pos = self._mover(pos, direccion)
                if nueva_pos not in self.visitados:
                    return direccion

        # 4. Si no hay opción → moverse a cualquier libre
        for direccion in self.ACCIONES:
            if percepcion[direccion] == 'libre':
                return direccion

        # 5. Último recurso
        return 'abajo'

    def _mover(self, pos, direccion):
        dr, dc = self.DELTAS[direccion]
        return (pos[0] + dr, pos[1] + dc)
