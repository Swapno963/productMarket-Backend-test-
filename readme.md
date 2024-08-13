# Daraz : E-commerce Platform

## Description

This project is a full-stack web e-commerce application built with React and Tailwind CSS. It provides various features for managing products.

- ** Get All Products -url: GET /products** : On the home page, users can view all products. On desktop, three products are displayed per row, while on mobile, only one product is displayed per row.

- **Add A New Product -url: POST /products**: Users can create a new product by clicking on "Create Product" in the navbar.

- **Update Product -url: PATCH /products** : Users can update a product by clicking on the three dots beside the product name and selecting "Edit."

- **Delete Product -url: DELETE PRODUCTS url**: Users can delete a product by clicking on the three dots beside the product name and selecting "Delete."

- **Detail Product -url: /products/id/** : By clicking on the product name, users can view the detailed description on the product detail page.

- **Pagenation Product -url: /products/?limit=1** : with ?limit user can ask how many product he wants

- **Pagenation Product -url: /products/?search=apple** : with ?search user can search on name of products.

### Authientication

- **Register Product -url: auth/register/**
- **Login Product -url: auth/login/**

## Live server link : https://product-market-backend-test.vercel.app/

## Live site : https://e-commerce-test-two.vercel.app/

## Technologies Used

- Django
- djangorestframework-simplejwt

## Setup instruction

### 1. Clone the Repository

```bash
git clone https://github.com/Swapno963/productMarket-Backend-test-

cd productMarket-Backend-test-

pip install -r requirements.txt

```

### 1. To run test case

```bash
 python manage.py test
```

## Accessing the Admin Panel

Please use the following credentials:

- **Username:** admin
- **Password:** 12
