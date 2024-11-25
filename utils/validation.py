"""
Author: MK Khodadadi
Latest Modification Date: November 25, 2024
"""

from pydantic import BaseModel
from typing import List


class BusinessHours(BaseModel):
    """
    A model representing business hours of a business.

    Attributes:
        formattedHours (List[str]): A list of strings representing the formatted business hours.
        nextStatusChange (str): The time when the business will next change its status.
        currentStatus (str): The current operational status of the business (e.g., Open, Closed).
    """
    formattedHours: List[str]
    nextStatusChange: str
    currentStatus: str


class ContactInfo(BaseModel):
    """
    A model representing contact information of a business.

    Attributes:
        phoneNumber (str): The phone number for contacting the business.
    """
    phoneNumber: str


class Position(BaseModel):
    """
    A model representing geographical position with latitude and longitude.

    Attributes:
        lat (float): The latitude of the business location.
        lng (float): The longitude of the business location.
    """
    lat: float
    lng: float


class PriceSummary(BaseModel):
    """
    A model representing the price summary of a business.

    Attributes:
        priceRangeLevel (str): The price range level (e.g., Low, Medium, High).
        free (bool): A boolean indicating if the business offers free services.
    """
    priceRangeLevel: str
    free: bool


class Reviews(BaseModel):
    """
    A model representing reviews of a business.

    Attributes:
        averageRating (float): The average rating of the business (e.g., 4.5).
        reviewCount (int): The total number of reviews.
    """
    averageRating: float
    reviewCount: int


class ParkingDimensionRestriction(BaseModel):
    """
    A model representing parking dimension restrictions.

    Attributes:
        height (float): The height limit for parking (in meters or feet).
        width (float): The width limit for parking (in meters or feet).
    """
    height: float
    width: float


class Parking(BaseModel):
    """
    A model representing parking information for a business.

    Attributes:
        spotsNumber (int): The total number of parking spots.
        freeSpotsNumber (int): The number of free parking spots.
        disabledSpotsNumber (int): The number of parking spots for disabled individuals.
        parkingDimensionRestriction (ParkingDimensionRestriction): Parking dimension restrictions.
        services (List[str]): A list of services provided in the parking area.
        types (List[str]): A list of parking types available (e.g., Covered, Open).
        operator (str): The operator responsible for the parking area.
    """
    spotsNumber: int
    freeSpotsNumber: int
    disabledSpotsNumber: int
    parkingDimensionRestriction: ParkingDimensionRestriction
    services: List[str]
    types: List[str]
    operator: str


class ListPrices(BaseModel):
    """
    A model representing a specific service and its price.

    Attributes:
        service (str): The name of the service.
        price (str): The price for the service.
    """
    service: str
    price: str


class PriceStructured(BaseModel):
    """
    A model representing structured price information for a business.

    Attributes:
        listPrices (ListPrices): A list of services and their corresponding prices.
    """
    listPrices: ListPrices


class SushiValidator(BaseModel):
    """
    A model to validate sushi-related business information.

    Attributes:
        address (str): The address of the business.
        businessHours (BusinessHours): The business hours information.
        categories (List[str]): A list of categories the business belongs to.
        contactInfo (ContactInfo): The contact information of the business.
        distance_from_current_location (str): The distance from the current location to the business.
        duration_from_current_location (str): The time duration from the current location to the business.
        foodTypes (List[str]): A list of food types offered by the business (e.g., Sushi, Ramen).
        position (Position): The geographical position of the business.
        priceSummary (PriceSummary): The price summary of the business.
        reviews (Reviews): The review information for the business.
        title (str): The title or name of the business.
    """
    address: str
    businessHours: BusinessHours
    categories: List[str]
    contactInfo: ContactInfo
    distance_from_current_location: str
    duration_from_current_location: str
    foodTypes: List[str]
    position: Position
    priceSummary: PriceSummary
    reviews: Reviews
    title: str


class ParkingValidator(BaseModel):
    """
    A model to validate parking-related business information.

    Attributes:
        address (str): The address of the business.
        availability (str): The parking availability status (e.g., Available, Full).
        businessHours (BusinessHours): The business hours information.
        categories (List[str]): A list of categories the business belongs to.
        contactInfo (ContactInfo): The contact information of the business.
        distance_from_current_location (str): The distance from the current location to the business.
        duration_from_current_location (str): The time duration from the current location to the business.
        parking (Parking): The parking information for the business.
        paymentMethods (List[str]): A list of accepted payment methods in the parking area.
        position (Position): The geographical position of the business.
        priceStructured (PriceStructured): The structured pricing information for the business.
        priceSummary (PriceSummary): The price summary for the business.
        title (str): The title or name of the business.
    """
    address: str
    availability: str
    businessHours: BusinessHours
    categories: List[str]
    contactInfo: ContactInfo
    distance_from_current_location: str
    duration_from_current_location: str
    parking: Parking
    paymentMethods: List[str]
    position: Position
    priceStructured: PriceStructured
    priceSummary: PriceSummary
    title: str
