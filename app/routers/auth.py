from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.core.session import get_db
from app.models.user import User
from app.core.security import hash_password

router = APIRouter()


@router.post("/register")
def registr(data: dict, db: Session = Depends(get_db)):
    try:
        loggin = data.get("loggin").lower()
        password = data.get("password")

        if not loggin or not password:
            raise HTTPException(status_code=400, detail="Missing loggin or password")

        user_exists = db.query(User).filter(User.loggin == loggin.lower()).first()
        if user_exists:
            raise HTTPException(status_code=400, detail="login_is_busy")

        new_user = User(loggin=loggin, password_hash=hash_password(password))
        db.add(new_user)
        try:
            db.commit()
        except:
            db.rollback()
            raise HTTPException(status_code=400, detail='Login is already taken (DB Constraint) ')

        db.refresh(new_user)
        return {"message": "registration_successful"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error!!!")
