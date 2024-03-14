from fastapi import APIRouter

router = APIRouter(prefix="/contas-a-pagar-e-receber")

@router.get("/")
def listar_contas():
    return[
        {"conta1":"contas1"},
        {"conta2":"contas2"},
    ]

