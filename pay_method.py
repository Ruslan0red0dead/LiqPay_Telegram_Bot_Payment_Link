from liqpay.liqpay3 import LiqPay

public_key = ''
private_key = ''

liqpay = LiqPay(public_key, private_key)
def payment_details(amount:int,description:str,order_id:int):
    params = {
    'action': 'pay',
    'amount': amount,
    'currency': 'USD',
    'description': description,
    'order_id': order_id,
    'version': '3'
    }

    data_value = liqpay.cnb_data(params)
    signature_value = liqpay.cnb_signature(params)

    return f"https://www.liqpay.ua/api/3/checkout/?data={data_value}&signature={signature_value}"


# # Перевірка статусу платежу
# def payment_status(order_id):
#     res = liqpay.api("request", {
#         "action"        : "status",
#         "version"       : "3",
#         "order_id"      : order_id
#         })

#     return res