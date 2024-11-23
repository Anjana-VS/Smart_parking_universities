from app.models import ParkingSlot, db

def allocate_slot(license_plate):
    slot = ParkingSlot.query.filter_by(is_occupied=False).first()
    if slot:
        slot.is_occupied = True
        db.session.commit()
        return slot
    return None
