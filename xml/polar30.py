{
	"EXML": {
		"@version": "2.2.0.0",
		"defines": {
			"experiment": {
				"@ID": "0",
				"name": "Retinotopic Mapping Experiment with the use of a TriggerTimer or ParallelPort",
				"debugmode": "false"
			}
		},
		"declarations": {
			"object": [{
				"@ID": "2",
				"class": "ParallelPort",
				"name": "ParallelPort_Object_1",
				"constructor": {
					"param1": null
				}
			}, {
				"@ID": "0",
				"class": "TriggerTimer",
				"name": "Timer_Object_1",
				"constructor": {
					"param1": null
				}
			}, {
				"@ID": "1",
				"class": "RetinotopyMapper",
				"name": "RetinoMap_RenderWidgetGL",
				"constructor": {
					"param1": null
				}
			}]
		},
		"connections": {
			"object": [{
				"@ID": "2",
				"type": "signal",
				"signature": "CaptureThreadTriggered(short)",
				"target": {
					"@ID": "1",
					"type": "slot",
					"signature": "incrementExternalTrigger()"
				}
			}, {
				"@ID": "0",
				"type": "signal",
				"signature": "timeout()",
				"target": {
					"@ID": "1",
					"type": "slot",
					"signature": "incrementExternalTrigger()"
				}
			}]
		},
		"initializations": {
			"object": [{
				"@ID": "2",
				"type": "slot",
				"signature": "StartCaptureThread",
				"parameters": {
					"parameter": [{
						"@ID": "0",
						"name": "baseAddress",
						"value": "889",
						"type": "const short"
					}, {
						"@ID": "1",
						"name": "mask",
						"value": "32",
						"type": "const short"
					}, {
						"@ID": "2",
						"name": "method",
						"value": "2",
						"type": "const short"
					}, {
						"@ID": "3",
						"name": "postLHDelay",
						"value": "100",
						"type": "const int"
					}, {
						"@ID": "4",
						"name": "postHLDelay",
						"value": "100",
						"type": "const int"
					}]
				}
			}, {
				"@ID": "0",
				"type": "slot",
				"signature": "startTimer",
				"parameters": {
					"parameter": {
						"@ID": "0",
						"name": "msec",
						"value": "1000",
						"type": "double"
					}
				}
			}]
		},
		"actions": {
			"blocks": {
				"block": [{
					"@ID": "0",
					"name": "Fixation_Block",
					"block_number": "0",
					"nr_of_trials": "1",
					"nr_of_internal_triggers": "2",
					"nr_of_external_triggers": "1",
					"object": {
						"@ID": "1",
						"parameters": {
							"parameter": [{
								"@ID": "0",
								"name": "RetinoPattern",
								"value": "fixation"
							}, {
								"@ID": "1",
								"name": "ShowFixPoint",
								"value": "true"
							}, {
								"@ID": "2",
								"name": "InternalTriggerDuration",
								"value": "1000"
							}, {
								"@ID": "3",
								"name": "OutputTriggerFrame",
								"value": "false"
							}, {
								"@ID": "4",
								"name": "OutputFrameType",
								"value": "Mask"
							}, {
								"@ID": "5",
								"name": "AntiAliasing",
								"value": "true"
							}, {
								"@ID": "6",
								"name": "StimulusWidthSpan",
								"value": "768"
							}, {
								"@ID": "7",
								"name": "StimulusHeightSpan",
								"value": "768"
							}, {
								"@ID": "8",
								"name": "OutputFrameFormat",
								"value": "PNG"
							}, {
								"@ID": "10",
								"name": "FixationSize",
								"value": "12"
							}, {
								"@ID": "11",
								"name": "CycleTriggerAmount",
								"value": "1"
							}, {
								"@ID": "12",
								"name": "StimuliRefreshRate",
								"value": "30"
							}, {
								"@ID": "13",
								"name": "BackGroundColor",
								"value": "#575757"
							}, {
								"@ID": "14",
								"name": "FixationColor",
								"value": "#FF0000"
							}, {
								"@ID": "15",
								"name": "CheckerColor1",
								"value": "#FFFFFF"
							}, {
								"@ID": "16",
								"name": "CheckerColor2",
								"value": "#000000"
							}]
						}
					}
				}, {
					"@ID": "1",
					"name": "PolarAngle_Block",
					"block_number": "1",
					"nr_of_trials": "6",
					"nr_of_internal_triggers": "36",
					"nr_of_external_triggers": "1",
					"object": {
						"@ID": "1",
						"parameters": {
							"parameter": [{
								"@ID": "0",
								"name": "ShowFixPoint",
								"value": "true"
							}, {
								"@ID": "1",
								"name": "CycleTriggerAmount",
								"value": "12"
							}, {
								"@ID": "2",
								"name": "EmptyTriggerSteps",
								"value": "0"
							}, {
								"@ID": "3",
								"name": "PolarWedgeSpan",
								"value": "30"
							}, {
								"@ID": "4",
								"name": "PolarCheckAmount",
								"value": "12"
							}, {
								"@ID": "5",
								"name": "PolarRingAmount",
								"value": "10"
							}, {
								"@ID": "6",
								"name": "PolarRotationDirection",
								"value": "1"
							}, {
								"@ID": "7",
								"name": "FlickrFrequency",
								"value": "7.5"
							}, {
								"@ID": "8",
								"name": "CorticalMagnitudeFactor",
								"value": "0"
							}, {
								"@ID": "9",
								"name": "RetinoPattern",
								"value": "PolarAngle"
							}, {
								"@ID": "10",
								"name": "GapDiameter",
								"value": "50"
							}, {
								"@ID": "11",
								"name": "DiscreteTriggerSteps",
								"value": "false"
							}, {
								"@ID": "12",
								"name": "RandomizeTriggerSteps",
								"value": "false"
							}, {
								"@ID": "12",
								"name": "DisableCortMagFac",
								"value": "true"
							}]
						}
					}
				}, {
					"@ID": "2",
					"name": "Fixation_Block",
					"block_number": "2",
					"nr_of_trials": "1",
					"nr_of_internal_triggers": "8",
					"nr_of_external_triggers": "1",
					"object": {
						"@ID": "1",
						"parameters": {
							"parameter": [{
								"@ID": "0",
								"name": "RetinoPattern",
								"value": "fixation"
							}, {
								"@ID": "1",
								"name": "ShowFixPoint",
								"value": "true"
							}]
						}
					}
				}]
			}
		},
		"finalizations": {
			"object": [{
				"@ID": "0",
				"type": "slot",
				"signature": "stopTimer"
			}, {
				"@ID": "2",
				"type": "slot",
				"signature": "StopCaptureThread"
			}]
		}
	}
}
