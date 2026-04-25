from google.genai.types import Part
import datetime

timezone = datetime.timezone(datetime.timedelta(hours=-4))  # UTC-4 para Caracas

def get_current_datetime():
    """
    Devuelve la fecha y hora actual en formato ISO 8601 con zona horaria de Caracas (UTC-4).
    """
    now = datetime.datetime.now(tz=timezone)
    return now.isoformat()

def get_current_time():
    """
    Devuelve la hora actual en formato ISO 8601 con zona horaria de Caracas (UTC-4).
    """
    now = datetime.datetime.now(tz=timezone)
    return now.time()

def get_current_weekday(day: str = None):
    """
    Devuelve el día de la semana actual o de un día específico en formato ISO 8601 con zona horaria de Caracas (UTC-4).

    Args:
        day (str, optional): The date for which to get the weekday, in YYYY-MM-DD format.
    """
    if day:
        try: now = datetime.datetime.strptime(day, "%Y-%m-%d")
        except ValueError: return "Formato de fecha inválido. Use YYYY-MM-DD."
    
    now = datetime.datetime.now(tz=timezone)
    return now.strftime("%A")

time_function_content = [
    Part.from_function_call(name='get_current_datetime'),
    Part.from_function_call(name='get_current_time'),
    Part.from_function_call(name='get_current_weekday'),
]


if __name__ == "__main__":
    print(f"Fecha y hora actual: {get_current_datetime()}")
    print(f"hora actual:         {get_current_time()}")
    print(f"dia de la semana:    {get_current_weekday()}")