import uvicorn
from fastapi import FastAPI
from ContasAPagarEReceber import contas_a_pagar_e_receber_router

app = FastAPI()

app.include_router(contas_a_pagar_e_receber_router.router)

if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.1", port=8001)






