<template>
    <div class="page-checkout">
        <div class="column is-multiline">
            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>
            <div class="colums is-12">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in cart.items"
                        v-bind:key="item.product.id"
                        >
                        <td>{{ item.product.name }}</td>
                        <td>{{ item.product.price }}</td>
                        <td>{{ item.quantity }}</td>
                        <td>${{ getItemTotal(item).toFixed(2) }}</td>
                        </tr>
                    </tbody>
                    <tfoot>
                        <tr>
                            <td colspan="2">Total</td>
                            <td>{{ cartTotalLength }}</td>
                            <td>{{ cartTotalPrice }}</td>
                        </tr>
                    </tfoot>
                </table>
            </div>
            <div class="column is-12 box">
                <h2 class="subtitle">Shipping details</h2>
                <p class="has-text-grey mb-4">* All fields are required</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { computed } from 'vue'
export default {
    name: 'CheckoutView',
    data() {
        return {
            cart: {
                items: []
            },
            stripe: {},
            card: {},
            first_name: '',
            last_name: '',
            email: '',
            phone: '',
            address: '',
            zipcode: '',
            place: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Checkout | Djackets'
        this.cart = this.$store.state.cart
        console.log("Logging cart"+JSON.stringify(this.cart))
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
    },
    computed: {
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                console.log("Current Val "+JSON.stringify(curVal))
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        }
    }
}
</script>