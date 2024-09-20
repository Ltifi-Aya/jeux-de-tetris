import time

class Timer:
    def __init__(self, interval):
        """
        Initialise le timer avec un intervalle spécifié.
        """
        self.interval = interval
        self.last_time = time.time()

    def check(self):
        """
        Vérifie si l'intervalle de temps est écoulé depuis le dernier déclenchement.
        """
        current_time = time.time()
        if current_time - self.last_time >= self.interval:
            self.last_time = current_time
            return True
        return False

    def reset(self):
        """
        Réinitialise le timer.
        """
        self.last_time = time.time()
