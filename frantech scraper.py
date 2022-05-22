import requests


def get_cookies():
    return {"BUYVM": requests.get("https://my.frantech.ca/cart.php").text.split("BUYVM=")[1].split("\";")[0]} 


def get_gids(cookies):
    return list(map(lambda gid : gid.split("\">")[0],  requests.get("https://my.frantech.ca/cart.php", cookies=cookies).text.split("panel-title")[0].split("?gid=")[1::1]))


def print_product_info(product):
    info = {"name": product.split("package-name\">")[1].split("</h3")[0], "price": product.split("price-prefix\">$</span>")[1].split("<")[0], "pid": product.split("package-footer\">\n                                <a href=\"cart.php?a=add&pid=")[1].split("\" class=")[0]}
    info["url"] = "https://my.frantech.ca/aff.php?aff=5737&pid=" + info["pid"]
    if "package-qty" in product:
        info["quantity"]= int(product.split("package-qty\">\n                                        ")[1].split(" Available\n                                    </div")[0])
    print(info)


def print_pids(gids, cookies):
    list(map(lambda gid : list(map(lambda p : print_product_info(p), requests.get(f"https://my.frantech.ca/cart.php?gid={gid}", cookies=cookies).text.split("col-lg-4 col-sm-6")[1::1])), gids))


if __name__ == "__main__":
   cookies = get_cookies()
   gids = get_gids(cookies)
   print_pids(gids, cookies)