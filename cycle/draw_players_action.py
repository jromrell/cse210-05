from execution import Execution
from players import Players
class DrawPlayersAction(Execution):
    """
    An output action that draws all the actors.
    The responsibility of DrawActorsAction is to draw all the actors.
    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """
    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service
    def execute(self, contestants, script):
        """Executes the draw actors action.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score = Players.get_move_next("scores")
        snake = contestants.get_first_actor("snakes")
        segments = snake.get_segments()
        messages = contestants.get_actors("messages")
        self._video_service.clear_buffer()
        self._video_service.draw_actors(segments)
        self._video_service.draw_actor(score)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()