from sqlalchemy import create_engine, text

"""db_connection_string = "mysql://2MarNVgMbkgBoNS.root:RnQDXvM0Zs4GT2DS@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test" """

db_connection_string = "mysql+mysqldb://2MarNVgMbkgBoNS.root:RnQDXvM0Zs4GT2DS@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test?ssl_mode=VERIFY_IDENTITY&ssl_ca=/etc/ssl/certs/ca-certificates.crt"

engine = create_engine(db_connection_string)

# engine = create_engine(db_connection_string)

# with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))

#     result_dicts = []
#     for row in result.all():
#         result_dicts.append(dict(row._mapping))

#     print(result_dicts)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    # Let's check the type of the result: We are doing this beacuse we have to work on types of the data. That's why we are working on this.
    # print("The type of the result is:",type(result))
    result_all = result.all()
    # print("\nThe type of the result_all is the:",type(result_all))
    # print("The final result is the:",result_all)
    print(type(result_all))

    # Let's convert sqlalchemy row into the dictionary:
    # first_result = result_all[0]
    # first_result_dict = dict(result_all[1])
    # print("type(first_result_dict())",(type(first_result_dict)))
    # print(first_result_dict)