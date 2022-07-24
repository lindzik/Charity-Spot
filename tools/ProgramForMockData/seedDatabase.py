import psycopg2
import random

try:
    connection = psycopg2.connect(user="seal_team",
                                  password="seal_team",
                                  host="localhost",
                                  port="5432",
                                  database="main")

    cursor = connection.cursor()

    #OrgID = UserID

    #clear tables first

    postgres_delete_query = "DELETE FROM public.user;"
    cursor.execute(postgres_delete_query)
    connection.commit()

    postgres_delete_query = "DELETE FROM public.donation_item;"
    cursor.execute(postgres_delete_query)
    connection.commit()

    #Each charity makes 30 donations with small variations in type and location


    #1 Edgars
    postgres_insert_query = "INSERT INTO public.user (user_id, email, password, password_salt, identity) VALUES (%s,%s,%s,%s,%s);"
    record_to_insert = ("1", "edgars@email.com", "1234", "edgars@email.com#", "temp")
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()

    #Edgards makes 50% of donations in Cape Town and 50% in Pretoria. Always clothes

    for x in range(15):

        month = random.randint(1,12)
        day = random.randint(1,28)

        postgres_insert_query = "INSERT INTO public.donation_item (item_name, org_id, quantity, descrition, picture, quality, type, item_id, dono_date, dono_loc) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        record_to_insert = (f"Clothing item {x} from Edgars. Pretoria", "1", "1", "This is a clothing item", "DonatedItems/cl5zazk0p00271xchzb79mksy.jpeg", "NEW", "CLOTHING", f"1{x}", f"{day},{month}", "Pretoria")
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()

    for x in range(15):

        month = random.randint(1,12)
        day = random.randint(1,28)

        postgres_insert_query = "INSERT INTO public.donation_item (item_name, org_id, quantity, descrition, picture, quality, type, item_id, dono_date, dono_loc) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        record_to_insert = (f"Clothing item {x} from Edgars. Cape Town", "1", "1", "This is a clothing item", "DonatedItems/cl5zazk0p00271xchzb79mksy.jpeg", "NEW", "CLOTHING", f"111{x}", f"{day},{month}", "Cape Town")
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        

    #2 Mr Price
    postgres_insert_query = "INSERT INTO public.user (user_id, email, password, password_salt, identity) VALUES (%s,%s,%s,%s,%s);"
    record_to_insert = ("2", "mr_price@email.com", "1234", "mr_price@email.com#", "temp")
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()

    #3 Scooters Pizza
    postgres_insert_query = "INSERT INTO public.user (user_id, email, password, password_salt, identity) VALUES (%s,%s,%s,%s,%s);"
    record_to_insert = ("3", "scooters_pizza@email.com", "1234", "scooters_pizza@email.com#", "temp")
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()

    #4 Checkers
    postgres_insert_query = "INSERT INTO public.user (user_id, email, password, password_salt, identity) VALUES (%s,%s,%s,%s,%s);"
    record_to_insert = ("4", "checkers@email.com", "1234", "checkers@email.com#", "temp")
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()

    #5 Spar
    postgres_insert_query = "INSERT INTO public.user (user_id, email, password, password_salt, identity) VALUES (%s,%s,%s,%s,%s);"
    record_to_insert = ("5", "spar@email.com", "1234", "spar@email.com#", "temp")
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()

    #6 Clicks
    postgres_insert_query = "INSERT INTO public.user (user_id, email, password, password_salt, identity) VALUES (%s,%s,%s,%s,%s);"
    record_to_insert = ("6", "clicks@email.com", "1234", "clicks@email.com#", "temp")
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()

    #7 The Clothing Store
    postgres_insert_query = "INSERT INTO public.user (user_id, email, password, password_salt, identity) VALUES (%s,%s,%s,%s,%s);"
    record_to_insert = ("7", "the_clothing_store@email.com", "1234", "the_clothing_store@email.com#", "temp")
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()

    #8 The General Store
    postgres_insert_query = "INSERT INTO public.user (user_id, email, password, password_salt, identity) VALUES (%s,%s,%s,%s,%s);"
    record_to_insert = ("8", "the_general_store@email.com", "1234", "the_general_store@email.com#", "temp")
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()

    #9 Pretoria Restaurant
    postgres_insert_query = "INSERT INTO public.user (user_id, email, password, password_salt, identity) VALUES (%s,%s,%s,%s,%s);"
    record_to_insert = ("9", "pretoria_restaurant@email.com", "1234", "pretoria_restaurant@email.com#", "temp")
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()

    #10 Cape Town Restaurant
    postgres_insert_query = "INSERT INTO public.user (user_id, email, password, password_salt, identity) VALUES (%s,%s,%s,%s,%s);"
    record_to_insert = ("10", "cape_town_restaurant@email.com", "1234", "cape_town_restaurant@email.com#", "temp")
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()

    #11 Durban Clothing Store
    postgres_insert_query = "INSERT INTO public.user (user_id, email, password, password_salt, identity) VALUES (%s,%s,%s,%s,%s);"
    record_to_insert = ("11", "durban_clothing_store@email.com", "1234", "durban_clothing_store@email.com#", "temp")
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()

    #12 Woolworths
    postgres_insert_query = "INSERT INTO public.user (user_id, email, password, password_salt, identity) VALUES (%s,%s,%s,%s,%s);"
    record_to_insert = ("12", "woolworths@email.com", "1234", "woolworths@email.com#", "temp")
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()

    #13 PEP
    postgres_insert_query = "INSERT INTO public.user (user_id, email, password, password_salt, identity) VALUES (%s,%s,%s,%s,%s);"
    record_to_insert = ("13", "pep@email.com", "1234", "pep@email.com#", "temp")
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()

    #14 Discount Clothing Store
    postgres_insert_query = "INSERT INTO public.user (user_id, email, password, password_salt, identity) VALUES (%s,%s,%s,%s,%s);"
    record_to_insert = ("14", "discount_clothing_store@email.com", "1234", "discount_clothing_store@email.com#", "temp")
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()

    #15 Pick n Pay
    postgres_insert_query = "INSERT INTO public.user (user_id, email, password, password_salt, identity) VALUES (%s,%s,%s,%s,%s);"
    record_to_insert = ("15", "pick_n_pay@email.com", "1234", "pick_n_pay@email.com#", "temp")
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()

    #16 Ackermans
    postgres_insert_query = "INSERT INTO public.user (user_id, email, password, password_salt, identity) VALUES (%s,%s,%s,%s,%s);"
    record_to_insert = ("16", "ackermans@email.com", "1234", "ackermans@email.com#", "temp")
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()

    #17 Shoprite
    postgres_insert_query = "INSERT INTO public.user (user_id, email, password, password_salt, identity) VALUES (%s,%s,%s,%s,%s);"
    record_to_insert = ("17", "shoprite@email.com", "1234", "shoprite@email.com#", "temp")
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()

    #18 Dischem
    postgres_insert_query = "INSERT INTO public.user (user_id, email, password, password_salt, identity) VALUES (%s,%s,%s,%s,%s);"
    record_to_insert = ("18", "dischem@email.com", "1234", "dischem@email.com#", "temp")
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()

    #19 West Pack
    postgres_insert_query = "INSERT INTO public.user (user_id, email, password, password_salt, identity) VALUES (%s,%s,%s,%s,%s);"
    record_to_insert = ("19", "west_pack@email.com", "1234", "west_pack@email.com#", "temp")
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()

    #20 OK Furniture
    postgres_insert_query = "INSERT INTO public.user (user_id, email, password, password_salt, identity) VALUES (%s,%s,%s,%s,%s);"
    record_to_insert = ("20", "ok_furniture@email.com", "1234", "ok_furniture@email.com#", "temp")
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")