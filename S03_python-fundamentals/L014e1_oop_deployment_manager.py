class Deployment:
    """
    Manages the state and version history of a software deployment.
    """

    def __init__(self, service_name: str, environment: str):
        self.service_name      = service_name
        self.environment       = environment
        self.status            = 'pending'
        self._current_version  = None
        self._previous_version = None

    def deploy(self, new_version: str):
        self._previous_version = self._current_version
        self._current_version  = new_version
        self.status            = 'deployed'

    def rollback(self) -> bool:
        if self._previous_version is None:
            return False
        self._current_version  = self._previous_version
        self._previous_version = None
        self.status         = 'rolled_back'
        return True

    def check_status(self) -> dict:
        return {
            'service_name': self.service_name,
            'environment': self.environment,
            'status': self.status,
            'version': self._current_version,
        }