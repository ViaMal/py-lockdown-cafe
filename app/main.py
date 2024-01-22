from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    mask_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            mask_to_buy += 1
        except VaccineError:
            return "All friends should be vaccinated"

    if mask_to_buy > 0:
        return f"Friends should buy {mask_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
