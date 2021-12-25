import generators
import queries
import logics


logics.Simple_logic(
    login_generator=generators.ListGenerator(tokens=['admin', 'jack', 'cat']),
    password_generator=generators.FileGenerator(filename='pop-pass.txt'),
    query=queries.local_server)
#
# logics.get_accounts_logic(
#     login_genrator= generators.FileGenerator(filename='pop-pass.txt '),
#     password_generator=generators.FileGenerator(filename='pop-pass.txt'),
#     query=queries.local_server
#
# )
#
#
# logics.get_accounts_logic(
#
#     login_genrator=generators.ListGenerator(tokens=['admin', 'jack', 'cat']),
#     password_genrator=generators.BruteForseGenerator(),
#     query = queries.local_server,
#     password_limit=1000000
# )
#
#
# logics.get_password_logic(
#     login_genrator= generators.ListGenerator(tokens=['admin', 'jack', 'cat']),
#     password_generator= generators.FileGenerator(filename='pop-pass.txt'),
#     query= queries.local_server_protected
#     )

# протестируйте уже на своем сервере


